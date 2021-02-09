from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . import forms as f


@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/account')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main/changePassword.html', {'form': form})


@login_required()
def email_change(request):
    if request.method == 'POST':
        form = f.EmailChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/account")
    else:
        form = f.EmailChangeForm(request.user)
    return render(request, "main/changeEmail.html", {'form': form})


def home(response):
    return render(response, "main/home.html", {})


@login_required()
def account(request):
    profile = request.user
    return render(request, "main/account.html", {"profile": profile})
