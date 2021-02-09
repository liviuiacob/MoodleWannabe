from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice
from course.models import Group, Users


def index(request):
    grup = []
    user = Users.objects.all()
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    for x in user:
        if request.user.username.strip() == x.username.strip():
            grup.append(x.group)

    for x in Group.objects.all():
        if x.teacher == request.user.first_name + " " + request.user.last_name:
            grup.append(x)

    count = len(grup)
    context = {'grup': grup, 'latest_question_list': latest_question_list, 'count': count}
    return render(request, 'quiz/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/results.html', {'question': question})


def respond(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'quiz/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('quiz'))
