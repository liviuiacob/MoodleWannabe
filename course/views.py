import os

from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *
from .models import *
from main.models import Student, Teacher


def studentGroup(request):
    grup = Group.objects.all()
    utilizatori = Users.objects.all()
    fisiere=Fisier.objects.all()
    grupuri=[]


    ceva = 'nimic'
    studenti = Student.objects.all()
    profi = Teacher.objects.all()
    for x in studenti:
        if request.user.username == x.username.strip():
            ceva = 'student'
    for x in profi:
        if request.user.username == x.username.strip():
            ceva = 'prof'
    if ceva =='student':
        for x in utilizatori:
            if request.user.username.strip() == x.username.strip():
                grupuri.append(x.group)
    elif ceva == 'prof':
        for x in grup:
            if x.teacher==request.user.first_name+" "+request.user.last_name:
                grupuri.append(x)
    context = {'grupuri': grupuri,
               'fisiere': fisiere}
    return render(request, 'course/studentGroups.html', context)

def groupApp(request):
    forums = Group.objects.all()
    count = forums.count()
    ceva = 'nimic'
    studenti = Student.objects.all()
    profi = Teacher.objects.all()
    f=[]
    for x in studenti:
        if request.user.username == x.username.strip():
            ceva = 'student'
    for x in profi:
        if request.user.username == x.username.strip():
            ceva = 'prof'

    if ceva =='prof':
        for x in forums:
            if x.teacher==request.user.first_name+" "+request.user.last_name:
                f.append(x)
        count=len(f)
    else:
        f=forums
    # print(ceva)
    context = {'ceva': ceva,
               'forums': f,
               'count': count}
    return render(request, 'course/groups.html', context)


def addGroup(request):
    form = CreateGroup()
    if request.method == 'POST':
        grup=Group(teacher=request.user.first_name+" "+request.user.last_name)
        form = CreateGroup(request.POST , instance=grup)
        if form.is_valid():
            form.save()
            return redirect('/course')
    context = {'form': form}
    return render(request, 'course/addGroup.html', context)


def addInUser(request):
    form = CreatePartialUser()

    if request.method == 'POST':
        addIn = Users(username=request.user.username, email=request.user.email)
        form = CreatePartialUser(request.POST, instance=addIn)
        code = request.POST.get('enrollCode')
        group = Group.objects.all()
        enrCode = 0
        for i in group:
            if int(request.POST.get('group')) == i.id:
                enrCode = i.code

        if enrCode == code:
            if form.is_valid():
                form.save()
                return redirect('/course')
        else:
            form = CreatePartialUser()
    context = {'form': form}
    return render(request, 'course/addInUser.html', context)


def uploadFile(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/course')
        print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'course/uploadFile.html', {'form': form})

def sendEmail(request):
    if request.method == 'POST':
        form = CreateMail(request.POST, request.FILES)
        if form.is_valid():
            print(settings.EMAIL_HOST_USER)
            content=request.POST.get('content','')
            to=request.POST.get('to','')
            email=EmailMessage(
                request.user.first_name+" "+request.user.last_name,
                content,
                settings.EMAIL_HOST_USER,
                [to],
                headers={'Reply-To': settings.EMAIL_HOST_USER}
            )
            if request.FILES:
                file=request.FILES['file']
                email.attach(file.name,file.read(),file.content_type)
                email.send()
            return redirect('/materials')
    else:
        form = CreateMail()
    return render(request, 'course/sendEmail.html', {'form': form})