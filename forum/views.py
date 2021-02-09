from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *
from .models import Forum


def forumApp(request):
    forums = Forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'forum/forum.html', context)


def addInForum(request):
    form = PartialCreateInForum()
    if request.method == 'POST':
        addIn = Forum(username=request.user.username, email=request.user.email)
        form = PartialCreateInForum(request.POST, instance=addIn)
        if form.is_valid():
            form.save()
            return redirect('/forum')
    context = {'form': form}
    return render(request, 'forum/addInForum.html', context)


def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/forum')
    context = {'form': form}
    return render(request, 'forum/addInDisscusion.html', context)