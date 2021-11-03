from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]

class Company(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField(max_length=255)
    timestamp = models.DateField(auto_now_add=True)



