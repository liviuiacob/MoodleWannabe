from django.db import models

# Create your models here.
from django.utils import timezone

from course.models import Group


class Question(models.Model):
    group = models.ForeignKey(Group, blank=True, on_delete=models.CASCADE, default=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
