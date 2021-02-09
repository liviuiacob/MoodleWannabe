from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    occupation=forms.MultipleChoiceField(choices=[('1','student'),('2','teacher')])
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name","occupation", "email", "password1", "password2"]
