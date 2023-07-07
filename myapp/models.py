from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class ItemDos(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


# User Model
class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.username
