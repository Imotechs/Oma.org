from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
import os
from tinytag import TinyTag
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    


class Artist(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=30, null=True,blank=True)
    photo = models.ImageField(default = 'media/default.PNG', upload_to = 'media/Artist_profiles/')
    account = models.FloatField(default=0)
    date_joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Logo/{}'.format(filename)

def user_directory_path_song(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    return 'user_{0}/{1}'.format(self.artist.id, filename)

def uploaded_path(instance,filename):
    now = datetime.datetime.now()
    time_str = ''.join(ch for ch in str(now) if ch.isalnum())
    num1 = time_str[0:4]
    num2 = time_str[5:7]
    return f"{num1}/{num2}"


class Album(models.Model):
    album_name = models.CharField(max_length=30, verbose_name='Title')
    album_logo = models.ImageField(default = 'media/default.PNG', upload_to = 'media/Album_logo/')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,null=True, blank = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,null=True, blank = True)
    uploaded_on = models.DateTimeField(auto_now=True)
    cost = models.FloatField(default = 0, verbose_name='Monetization cost,0 if Free')
    def __str__(self):
        return self.album_name

    def get_absolute_url(self):
        return reverse('albumdetail',kwargs = {'pk':self.pk})


class ArtistSong(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title= models.CharField(max_length = 30,blank= True,null=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, blank= True,null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL,blank= True,null=True)
    album_name = models.ForeignKey(Album, on_delete=models.SET_NULL,blank= True,null=True)
    song_logo= models.ImageField(default = 'media/default.PNG', upload_to = 'media/Song_logo/',blank= True,null=True)
    audio_file = models.FileField(upload_to = 'media/artist_songs/', blank= True,null=True)
    uploaded_on = models.DateTimeField(auto_now=True)

    # objects = ArtistSongManager()

    def __str__(self):
        return self.title
    def size(self):
        # tag = TinyTag.get(self.audio_file)
        song = self.audio_file
        size = song.size/(1024*1024)
        return f'{str(size)[:3]}MB'
    def duration(self):
        tag = TinyTag.get(os.getcwd() + self.audio_file.url)
        duration_ = tag.duration/60
        return f"{str(duration_)[:3]}Min"

class Song(models.Model):
    title= models.CharField(max_length = 30)
    artist= models.CharField(max_length = 30)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    song_logo= models.ImageField(upload_to = uploaded_path,blank= True,null=True)
    audio_file = models.FileField(upload_to = 'media/songs')
    likes = models.IntegerField(default=0)
    uploaded_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def size(self):
        song = self.audio_file
        size = song.size/(1024*1024)
        return f'{str(size)[:3]}MB'
    def duration(self):
        tag = TinyTag.get(os.getcwd() + self.audio_file.url)
        duration_ = tag.duration/60
        return f"{str(duration_)[:3]}Min"
    def get_absolute_url(self):
        return reverse('songdetail',kwargs = {'pk':self.pk})



class NewRelease(models.Model):
    title= models.CharField(max_length = 30)
    artist= models.CharField(max_length = 30)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    song_logo= models.ImageField(upload_to = uploaded_path,blank= True,null=True)
    audio_file = models.FileField(upload_to = 'media/songs')
    uploaded_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def size(self):
        # tag = TinyTag.get(self.audio_file)
        song = self.audio_file
        size = song.size/(1024*1024)
        return f'{str(size)[:3]}MB'
    def duration(self):
        tag = TinyTag.get(os.getcwd() + self.audio_file.url)
        duration_ = tag.duration/60
        return f"{str(duration_)[:3]}Min"
    def get_absolute_url(self):
        return reverse('releasedetails',kwargs = {'pk':self.pk})


class ShowSongs(models.Model):
    title= models.CharField(max_length = 30)
    artist= models.CharField(max_length = 30)
    genre = models.ForeignKey(Genre,null = True, on_delete=models.SET_NULL)
    song_logo= models.ImageField(upload_to = uploaded_path,blank= True,null=True)
    audio_file = models.FileField(upload_to = 'media/songs')
    likes = models.IntegerField(default=0)
    uploaded_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def size(self):
        # tag = TinyTag.get(self.audio_file)
        song = self.audio_file
        size = song.size/(1024*1024)
        return f'{str(size)[:3]}MB'
    def duration(self):
        tag = TinyTag.get(os.getcwd() + self.audio_file.url)
        duration_ = tag.duration/60
        return f"{str(duration_)[:3]}Min"
    def get_absolute_url(self):
        return reverse('showdetail',kwargs = {'pk':self.pk})



class Event(models.Model):
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL)
    title = models.CharField(max_length = 30)
    event_date = models.CharField(max_length = 30)
    event_time = models.CharField(max_length = 30)
    photo = models.ImageField(default = 'default.jpg',upload_to = uploaded_path,blank= True,null=True)
    general = models.FloatField(null=True,blank=True,verbose_name='General')
    regular = models.FloatField(null=True,blank=True,verbose_name='Regular')
    vip = models.FloatField(null=True,blank=True,verbose_name='VIP')
    location = models.CharField(max_length = 50)
    descriptions = models.TextField(default = '')
    tickets = models.IntegerField( blank = True, null = True)
    approved = models.BooleanField(default = False)
    cancel = models.BooleanField(default = False)
    uploaded_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('eventdetail',kwargs = {'pk':self.pk})


    
