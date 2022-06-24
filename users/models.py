from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Album,Event
# Create your models here.

class AlbumPayment(models.Model):
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL)
    album = models.ForeignKey(Album,null = True,on_delete=models.SET_NULL)
    transaction_id = models.CharField(max_length=20, blank=True)
    cost = models.CharField(max_length = 30)
    is_id = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    date_paid = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class EventPayment(models.Model):
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event,null = True,on_delete=models.SET_NULL)
    transaction_id = models.CharField(max_length=20, blank=True)
    cost = models.CharField(max_length = 30)
    is_id = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    date_paid = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class Mail(models.Model):
    name = models.CharField(max_length=30, blank = True)
    email = models.CharField(max_length=30,blank = True)
    phone=models.CharField(max_length=30,blank = True)
    subject = models.TextField(blank = True) 
    message = models.TextField(blank = True) 
    seen = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL)
    account = models.FloatField(default=0)