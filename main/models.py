from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    username=models.CharField(max_length=100,default="Ceva")
    first_name = models.CharField(max_length=100, default="Ceva")
    last_name= models.CharField(max_length=100, default="Ceva")
    email= models.CharField(max_length=100, default="Ceva")


    def __str__(self):
        return self.last_name + self.first_name


class Teacher(models.Model):
    username=models.CharField(max_length=100,default="Ceva")
    first_name = models.CharField(max_length=100, default="Ceva")
    last_name= models.CharField(max_length=100, default="Ceva")
    email= models.CharField(max_length=100, default="Ceva")


    def __str__(self):
        return self.last_name + self.first_name


