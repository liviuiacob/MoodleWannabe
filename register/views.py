from django.shortcuts import render, redirect
from .forms import RegisterForm
from main.models import Student, Teacher


# Create your views here.


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            if response.POST.get('occupation') == '1':
                stud = Student(username=response.POST.get('username'), first_name=response.POST.get('first_name'),
                               last_name=response.POST.get('last_name'), email=response.POST.get('email'))
                stud.save()
            if response.POST.get('occupation') == '2':
                teach = Teacher(username=response.POST.get('username'), first_name=response.POST.get('first_name'),
                                last_name=response.POST.get('last_name'), email=response.POST.get('email'))
                profile.is_staff = True
                profile.is_superuser = True
                teach.save()
            profile.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})