from unicodedata import name
from django.db import models

# Create your models here.

class signUp(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    address = models.CharField(max_length=100, default='')
    number = models.PositiveIntegerField(default='')
    password = models.CharField(default='', max_length=15)

    def __str__(self):
        return self.name
    

class Problems(models.Model):
    problem = models.CharField(max_length=30, default='')
    isappoved = models.BooleanField(default=False)
    owner  = models.ForeignKey(signUp, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.isappoved