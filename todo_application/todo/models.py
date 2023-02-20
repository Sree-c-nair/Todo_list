from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Register(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=150)


class Login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=150)


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    Description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering =['completed']