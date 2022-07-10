
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Album, Song, Event,Artist,ArtistSong,NewRelease,ShowSongs,Genre
from django.views.generic import DetailView,TemplateView,CreateView
from django.views.generic import View
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from users.models import AlbumPayment
from users.models import Mail
from django.contrib.auth.decorators import login_required
from users.news import local_news as get_local_news
# Create your views here.


def home(request):
    if request.method =='POST':
        search = request.POST.get('search')
        song = Song.objects.filter(
            Q(title__icontains=search) | Q(artist__icontains=search))
        song1 = ShowSongs.objects.filter(
            Q(title__icontains=search) | Q(artist__icontains=search))
        song2 = NewRelease.objects.filter(
            Q(title__icontains=search) | Q(artist__icontains=search))
        artist = Artist.objects.filter(
            Q(name__icontains=search))
        album = Album.objects.filter(
            Q(album_name__icontains=search))
        context = {
                'songs':song,
                'song1':song1,
                'song2':song2,
                'artists':artist,
                'albums':album,
                'total':song.count() + song1.count() + song2.count(),
                }
        return render(request,'mainapp/search.html',context)
        
    news = get_local_news()
    topsingle = Song.objects.all().order_by('-uploaded_on')
    newrelease = NewRelease.objects.all().order_by('-uploaded_on')
    events = Event.objects.filter(approved = True,cancel =False).order_by('-uploaded_on')[:3]
    artist = Artist.objects.all().order_by('-date_joined')[:10]
    songs = ShowSongs.objects.all().order_by('-uploaded_on')[:4]
    choice = ShowSongs.objects.all().order_by('-uploaded_on')
    genres = Genre.objects.all()

    context = {
        'files':topsingle,
        'events':events,
        'artists':artist,
        'newsongs':songs,
        'newrelease':newrelease,
        'choice':choice,
        'genres':genres,
        'allnews':news
    }
    return render(request,'mainapp/index.html',context)
    
class AlbumDetail(DetailView):
    model = Album
    template_name = 'mainapp/albums.html'

def freealbum(request,pk):
        freealbum = Album.objects.get(id = pk)
        if freealbum.cost >0.00:
            messages.info('You must pay for this album!')
            return  redirect('home')
        context={'album':freealbum}
        return render(request, 'mainapp/freealbums.html',context)

def Paidalbum(request,pk):
        album = Album.objects.get(id = pk)
        payment = AlbumPayment.objects.filter(user = request.user,album = album)
        if not payment[0].is_valid:
            messages.info(request,'You do not pay for this Album!')
            return  redirect('home')
        context={'album':album}
        return render(request, 'mainapp/freealbums.html',context)

#songs detail views 
class SongDetail(DetailView):
    model = Song
    template_name = 'mainapp/songdetail.html'

class NewReleaseDetail(DetailView):
    model = NewRelease
    template_name = 'mainapp/songdetail.html'

class ShowSongDetail(DetailView):
    model = ShowSongs
    template_name = 'mainapp/songdetail.html'
  

#download views
class SongDownloadView(DetailView):
    model = Song
    template_name = 'mainapp/songdownload.html'

class NewReleaseDownloadView(DetailView):
    model = NewRelease
    template_name = 'mainapp/songdetail.html'
#upload Album
# class CreateAlbum(UserPassesTestMixin,CreateView):
#     model =  Album
#     fields = ['cost']
#     success_url = '/users/profile'
#     template_name = 'users/createalbum.html'
#     def form_valid(self, form):
#         form.instance.album_name = self.request.POST['title']
#         form.instance.album_logo = self.request.FILES['file']
#         form.instance.artist = self.request.user.artist
#         print(form.instance.album_name)
#         return super().form_invalid(form)
#     def test_func(self):
#         if self.request.user.is_superuser or self.request.user.is_staff or self.request.user in Artist.objects.all():
#             return True
#         return False


@login_required
def profile(request):
    if request.method =="POST":
        if '1' in request.POST['s1']:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user = User.objects.get(id = request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request,'Your Profile is updated!')
            return redirect('profile')

    artist = Artist.objects.all()
    pay = AlbumPayment.objects.filter(user = request.user,is_valid = True)
    albums = Album.objects.all()
    myalbums = Album.objects.filter(user = request.user).order_by('-uploaded_on')
    newsongs = Song.objects.all().order_by('-uploaded_on')[:9]
    mysongs = ArtistSong.objects.filter(user = request.user)
    context = {
        'artists':artist,
        'albums':albums,
        'payalbums':pay,
        'newsongs':newsongs,
        'myalbums':myalbums,
        'mysongs':mysongs,
    }
    return render(request,'mainapp/profile.html',context)


def release(request):
    if request.method =="POST":
        genre = request.POST.get('genre')
        if genre == '' or genre == None:
            releases = NewRelease.objects.all().order_by('-uploaded_on')
            genres = Genre.objects.all()
            events = Event.objects.filter(approved = True,cancel = False)
            context ={
                'songs':releases,
                'genres':genres,
                'events':events,
            }
            return render(request,'mainapp/releases.html',context)         
        else:
            songs = NewRelease.objects.filter(genre = genre)
            genres = Genre.objects.all()
            events = Event.objects.filter(approved = True,cancel = False)

            context = {
                'songs':songs,
                'genres':genres,
                'events':events,
            }
            return render(request,'mainapp/releases.html',context)
        

    releases = NewRelease.objects.all().order_by('-uploaded_on')[:10]
    genres = Genre.objects.all()
    events = Event.objects.filter(approved = True,cancel = False)
    context ={
        'songs':releases,
        'genres':genres,
        'events':events,
    }
    return render(request,'mainapp/releases.html',context)

def albums(request):
    if request.method =='POST':
        albums = Album.objects.all().order_by('-uploaded_on')
        events = Event.objects.filter(approved = True,cancel = False).order_by('-uploaded_on')

        context ={
            'albums':albums,
            'events':events,
        }
        return render(request,'mainapp/allalbums.html',context)

    albums = Album.objects.all().order_by('-uploaded_on')[:10]
    events = Event.objects.filter(approved = True,cancel = False).order_by('-uploaded_on')

    context ={
        'albums':albums,
        'events':events,
    }
    return render(request,'mainapp/allalbums.html',context)


class EventDetail(DetailView):
    model  = Event
    template_name = 'mainapp/eventdetail.html'

class Realese(DetailView):
    model  = Album
    template_name = 'mainapp/release.html'

def artists(request):
    if request.method == 'POST':
        artists = Artist.objects.all().order_by('date_joined')
        events = Event.objects.filter(approved = True,cancel = False).order_by('-uploaded_on')
        context = {
            'artists':artists,
            'events':events,
        }
        return render(request,'mainapp/artists.html',context)
    artists = Artist.objects.all().order_by('date_joined')[:10]
    events = Event.objects.filter(approved = True,cancel = False).order_by('-uploaded_on')

    context = {
        'artists':artists,
        'events':events,
    }
    return render(request,'mainapp/artists.html',context)
def becomeartist(request):
    if request.method =="POST":
        user = Artist.objects.filter(user = request.user)
        if user:
            messages.success(request,'You have signed up already')
            return redirect('profile')
        else:
            name = request.POST['username']
            
            obj = Artist.objects.create(user = request.user,
            name = name,
            photo = request.FILES['file'],
            )

            obj.save()
            messages.success(request,'You are now an Artist')
            return redirect('profile')

    return render(request,'users/becomeartist.html')

def artistdetail(request,pk):
    artist = Artist.objects.get(id = pk)
    albums =Album.objects.filter(artist = artist)
    altist_songs = ArtistSong.objects.all()
    context ={
        'albums':albums,
        'artist':artist,
        'altist_songs':altist_songs,
    }
    return render(request,'mainapp/artistdetail.html',context)

def events(request):
    if request.method =='POST':
        search = request.POST.get('search')
        if search == '1':
            event = Event.objects.filter(approved = True,cancel = False,)
            context = {
                'events':event
                }
            return render(request,'mainapp/events.html',context)
        
        event = Event.objects.filter(approved = True,cancel = False,).filter(
            Q(title__icontains=search) | Q(location__icontains=search))
        context = {
            'events':event
            }
        return render(request,'mainapp/events.html',context)
    events = Event.objects.filter(approved = True,cancel = False,).order_by('-uploaded_on')[:5]
    context = {
        'events':events
        }
    return render(request,'mainapp/events.html',context)

def news(request):
    return render(request,'mainapp/news.html')

def terms(request):
    return render(request,'mainapp/privacy.html')

def about(request):
    return render(request,'mainapp/about.html')

def contact(request):
    if request.method =='POST':
        obj, created = Mail.objects.get_or_create(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            subject = request.POST['subject'],
            message = request.POST['message'],   
            )
        obj.save()
        messages.success(request,'Mail Sent!')
        return redirect ('/')

    return render(request,'mainapp/contacts.html')

def passreset(request):
    if request.method =="GET":
        opassword = request.GET['opassword']        
        password = request.GET['password']        
        cpassword = request.GET['cpassword']
        if password == cpassword:
            user = User.objects.get(id = request.user.id)
            test = user.check_password(opassword)
            if test:
                user.set_password(cpassword)
                user.save()
                messages.success(request,'Success!')
                return redirect('profile')
            else:
                messages.info(request,'Incorrect old password')
                return redirect('profile')
        else:
            messages.success(request,'Two new passwords do not match')
            return redirect('profile')


def post_event(request):
    if request.method =="POST":
        event_title = request.POST['event_name']       
        event_date = request.POST['event_date']        
        event_time = request.POST['event_time']     
        event_desc = request.POST['event_desc']   
        event_cent = request.POST['event_cent']
        file = request.FILES['file'],
    
        obj = Event(
            user = request.user,
            title = event_title,
            event_date = event_date,
            event_time = event_time,
            location = event_cent,
            descriptions = event_desc,
            photo = file[0],
            general = request.POST['general'] or None,
            regular = request.POST['regular'] or None,
            vip = request.POST['vip'] or None,
            tickets = request.POST['qty'] or None,

            )

        obj.save()
        messages.success(request,'Event Submited!')
        return redirect('profile')



def my_custom_error_view(request):
    return render(request,'500.html')

def page_not_found_view(request):
    return render(request,'404.html')
    
def page_restricted_view(request):
    return render(request,'403.html')
