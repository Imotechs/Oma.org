from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Album,Event
from users.paystack import Paystack
from django.urls import reverse
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
    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.transaction_id,self.cost)
        print(status)
        if status:
            if float(result['amount']/100) >= float(self.cost):
                self.is_valid = True
            self.save()
        if self.is_valid:
            return True
        else:
            return False

class EventPayment(models.Model):
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event,null = True,on_delete=models.SET_NULL)
    transaction_id = models.CharField(max_length=20, blank=True)
    event_code = models.CharField(max_length=20, blank=True)
    ticket = models.CharField(max_length=20, blank=True,null=True)
    cost = models.CharField(max_length = 30)
    is_id = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    date_paid = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.transaction_id,self.cost)
        print(status)
        if status:
            if float(result['amount']/100) >= float(self.cost):
                self.is_valid = True
            self.save()
        if self.is_valid:
            return True
        else:
            return False

class Mail(models.Model):
    name = models.CharField(max_length=30, blank = True)
    email = models.CharField(max_length=30,blank = True)
    phone=models.CharField(max_length=30,blank = True)
    subject = models.TextField(blank = True) 
    message = models.TextField(blank = True) 
    seen = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now=True)

class Account(models.Model):
    user =  models.OneToOneField(User,null = True,on_delete= models.SET_NULL)
    balance =  models.PositiveIntegerField(blank=True, default= 0)

    def __str__(self):
        return f"{self.user}'s"


class Withdrowal(models.Model):
    user = models.ForeignKey(User, null = True,on_delete=models.SET_NULL)
    amount = models.FloatField(default=0, verbose_name='Amount to withdraw')
    account_number = models.CharField(max_length=30,null=True,blank=True)
    account_name = models.CharField(max_length=30,null=True,blank=True)
    account_type = models.CharField(max_length=30,null=True,blank=True)
    bank = models.CharField(max_length=30,null=True,blank=True)
    date_placed = models.DateTimeField(blank=True)
    date_approved = models.DateTimeField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class Post(models.Model):
    title = models.CharField(null =True,blank=True,max_length=500)
    author = models.CharField(null =True,blank=True,max_length=50)
    description = models.TextField()
    source = models.CharField(null =True,blank=True,max_length=50)
    image = models.ImageField(null =True,blank=True, upload_to = 'media/news/')
    likes = models.ManyToManyField(User)
    uploaded_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):
        return reverse('news_detail',kwargs = {'pk':self.pk})

class Comment(models.Model):
    user = models.ForeignKey(User,related_name = 'user',null = True,on_delete=models.SET_NULL)
    post = models.ForeignKey(Post,null = True,on_delete=models.SET_NULL)
    comment = models.TextField()
    likes = models.ManyToManyField(User)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment[:10]
