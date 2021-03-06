from itertools import count
from unicodedata import name
from django.db import models

# Create your models here.

class signUp(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    address = models.CharField(max_length=100, default='')
    number = models.PositiveIntegerField(default='')
    password = models.CharField(default='', max_length=15)
    isvoted = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name
    

class Problems(models.Model):
    problem = models.CharField(max_length=30)
    
    userVotes = models.CharField(max_length=999999)

    # userVotes = models.ArrayField(models.ArrayField(models.IntegerField()))
    
    isappoved = models.BooleanField(default=False, null=True)
    count = models.IntegerField(default=1)
    owner  = models.ForeignKey(signUp, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.problem)

class Voting(models.Model):
    user  = models.ForeignKey(signUp, on_delete=models.CASCADE, null=True, blank=True)
    issue  = models.ForeignKey(Problems, on_delete=models.CASCADE, null=True, blank=True)



class ContactForm(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    subject = models.CharField(max_length=100, default='')
    message = models.CharField(max_length=1000, default='')
    
    def __str__(self):
        return self.name