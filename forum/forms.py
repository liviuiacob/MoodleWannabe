from django.forms import ModelForm

from .models import Forum, Discussion


class PartialCreateInForum(ModelForm):
    class Meta:
        model = Forum
        exclude=['username','email']


class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
