from django import forms
from django.forms import ModelForm
from .models import *


class CreateGroup(ModelForm):
    class Meta:
        model = Group
        exclude = ['teacher']


class CreatePartialUser(ModelForm):
    class Meta:
        model = Users
        exclude = ['username', 'email']


class UploadFileForm(ModelForm):
    class Meta:
        model = Fisier
        fields = "__all__"

class CreateMail(forms.Form):
    content = forms.CharField()
    to = forms.EmailField()
    file = forms.FileField()
