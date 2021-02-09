from django.db import models


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=200, default="anonymous")
    teacher = models.CharField(max_length=200, default="anonymous")
    code = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)


# child model
class Users(models.Model):
    group = models.ForeignKey(Group, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, default="anonymous")
    email = models.CharField(max_length=200, null=True)
    enrollCode = models.CharField(max_length=300, null=True)

    def __str__(self):
        return str(self.username)


# child model 2
class Fisier(models.Model):
    group = models.ForeignKey(Group, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="ceva", blank=True)
    fisier = models.FileField(upload_to='groups/')

    def __str__(self):
        return str(self.group.name)+" "+str(self.title)
