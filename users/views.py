from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView
from mainapp.models import (Album, Artist, Genre, 
NewRelease,Song,ArtistSong,Event, ShowSongs)
from users.forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.conf import settings
from users.models import EventPayment, Withdrowal,Account,Post,Comment
from django.utils import timezone

from .import news
import json
def register(request):
    if request.method == 'POST':

        if User.objects.filter(email = request.POST['email']):
            msg = 'Email Already registered!'
            form = UserRegistrationForm(request.POST)
            context = {
                'form':form,
                'msg':msg,
            }
            return render(request,'users/signup.html',context)

        else:   
            form = UserRegistrationForm(request.POST)
            try:
                if form.is_valid:
                    form.save()
                    username = form.cleaned_data.get('username')
                    user = User.objects.get(username = request.POST['username'])
                    # profile = Profile( 
                    #     uid = functions.get_user_id(),
                    #     user = user

                    # )
                    # profile.save()
                    messages.success(request, 'Your registration was succesful!')
                    return redirect('login')          
            except ValueError:
                form = UserRegistrationForm(request.POST)
                msg = 'Error!'
                context = {
                    'form':form,
                    'msg':msg,
                        }
                return render(request,'users/signup.html',context)
            except Exception as err:
                print('we have some issues', err)


    form = UserRegistrationForm()
    context = {
        'form':form
    }
    return render(request,'users/signup.html',context)

def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    return redirect('profile')
                else:
                    msg = 'User records have issues, contact Admin!'
                    return render(request,'users/signin.html', {'msg':msg})
            elif user is None:
                msg = 'Error in Login Credentials!'
                return render(request,'users/signin.html', {'msg':msg})
            
        except Exception as err:
            print('we hav an error:', err)
            return redirect('login')

    return render(request,'users/signin.html')

class CreateAlbum(LoginRequiredMixin,CreateView):
    model = Album
    fields = ['album_name','album_logo','genre','cost']
    template_name = 'users/makealbum.html'
    def form_valid(self, form):
        user,created = Artist.objects.get_or_create(user = self.request.user)
        form.instance.artist = user
        form.instance.user = self.request.user
        messages.success(self.request, 'Album Created,Upload Songs')
        return super().form_valid(form)


class ArtistAddSongView(LoginRequiredMixin,CreateView):
    model = ArtistSong
    fields = ['title','song_logo','audio_file']
    template_name = 'users/makesong.html'
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super(ArtistAddSongView,self).get_context_data(**kwargs)
        context['pk'] = Album.objects.get(id = self.kwargs.get('pk'))
        return context
    def form_valid(self, form):
        try:
            album = Album.objects.get(id = self.request.POST['pk'],user = User.objects.get(id = self.request.user.id))
            if album:
                user,created = Artist.objects.get_or_create(user = self.request.user)
                form.instance.artist = user
                form.instance.user = User.objects.get(id = self.request.user.id)
                form.instance.album_name_id = self.request.POST['pk']
                messages.success(self.request, f'Song Added to {album}!')
                return super().form_valid(form)
            else:    
                messages.info(self.request, f" FORBIDEN!! This Album is not your own.")
                return redirect('home')
        except Exception as e:
                    print('ERROR:',e)
                    messages.info(self.request, f" FORBIDEN!! This Album is not your own.")
                    return redirect('home')    

def about(request):
    event = Event.objects.get(id = 1)
    context = {
        'event':event,
    }
    return render(request,'mainapp/about.html',context)

class AddSongView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Song
    fields = ['title','artist','genre','song_logo','audio_file']
    template_name = 'users/create.html'
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False
class AddReleaseView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = NewRelease
    fields = ['title','artist','genre','song_logo','audio_file']
    template_name = 'users/create.html'
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False
class AddshowSongView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = ShowSongs
    fields = ['title','artist','genre','song_logo','audio_file']
    template_name = 'users/create.html'
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False   
        
def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False

class AddGenreView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Genre
    fields = ['name']
    template_name = 'users/create.html'
    success_url = '/'
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False

def Allsongs(request):
    if request.method =='POST':
        genre = request.POST.get('genre')
        if genre == '' or genre == None:
            return redirect('all_songs')
        else:
            songs = Song.objects.filter(genre = genre)
            genres = Genre.objects.all()
            context = {
                'songs':songs,
                'genres':genres
            }
            return render(request,'users/allsongs.html',context)
    songs = Song.objects.all()
    genres = Genre.objects.all()
    context = {
        'songs':songs,
        'genres':genres
    }
    return render(request,'users/allsongs.html',context)

def Allreleaase(request):
    if request.method =='POST':
        genre = request.POST.get('genre')
        if genre == '' or genre == None:
            return redirect('all_new_release')
        else:
            
            songs = NewRelease.objects.all()
            genres = Genre.objects.all()
            context = {
                'songs':songs,
                'genres':genres
            }
            return render(request,'users/allsongs.html',context)
    songs = NewRelease.objects.all()
    genres = Genre.objects.all()
    context = {
        'songs':songs,
        'genres':genres
    }
    return render(request,'users/allsongs.html',context)


class WithDraw(LoginRequiredMixin,CreateView):
    template_name = 'users/withdraw.html'
    model = Withdrowal
    fields = ['account_number','account_name','account_type','bank','amount']
    success_url = '/accounts/profile/'
   
    def form_valid(self, form):
        pendings = Withdrowal.objects.filter(user  = self.request.user, approved = False, cancel = False)
        if not pendings:
            try:
                account,created  = Account.objects.get_or_create(user = self.request.user)

                if float(self.request.POST['amount']) < float(account.balance):
                    if float(self.request.POST['amount'])>999:
                        if float(self.request.POST['amount'])<50000:
                            account.balance = account.balance - float(self.request.POST['amount'])
                            form.instance.user = self.request.user
                            form.instance.amount = float(self.request.POST['amount'])
                            form.instance.date_placed = timezone.now()
                            form.instance.account_number = self.request.POST.get('account_number')
                            form.instance.account_type = self.request.POST.get('account_type')
                            form.instance.account_name = self.request.POST.get('account_name')
                            form.instance.bank = self.request.POST.get('bank')
                            messages.success(self.request,'Your Withdrawal was placed Succesfully!')
                            return super().form_valid(form) 
                        else:
                            messages.info(self.request,'Withdrawal amount must be below or equal to 50000 ')
                            return redirect('withdraw')
                    else:
                        messages.info(self.request,'Withdrawal amount must be 1000 or above ')
                        return redirect('withdraw')
                else:
                    messages.info(self.request,'Insufficient Balance')
                    return redirect('withdraw')
            except Exception:
                    messages.info(self.request,'Insufficient Balance')
                    return redirect('withdraw')          

        else:
            messages.info(self.request, 'Sorry!!,We are working on your Last Pending transaction')
            return redirect('withdraw') 

@login_required
def my_events(request):
    events = Event.objects.filter(user = request.user)
    albums = Album.objects.filter(user = request.user)
    context = {
        'events':events,
        'albums':albums,
    }
    return render(request, 'users/myevents.html',context)  

class UserEventDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Event
    template_name = 'users/event_detail.html'

    def test_func(self,*args,**kwargs):
        request = self.request
        event = self.get_object()
        if request.user.is_superuser or request.user == event.user:
            return True
        return False

class UserAlbumDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Album
    template_name = 'users/album_detail.html'

    def test_func(self,*args,**kwargs):
        request = self.request
        album = self.get_object()
        if request.user.is_superuser or request.user == album.user:
            return True
        return False


def my_news(request):
    try:
        celeb = news.get_celeb_news()
        music = news.get_music_news()
        locals = news.local_news()
        context = {
            'allnews':music,
            'celebnews':celeb,
            'locals':locals,
        }
        return render(request,'users/news.html',context)
    except Exception:
        music = news.get_music_news()
        locals = news.local_news()
        #cat = 'author title description url source image category language country published_at'
        context = {
            'allnews':music,
            'locals':locals,
        }
        return render(request,'users/news.html',context)
    except:
        locals = news.local_news()
       
        #cat = 'author title description url source image category language country published_at'
        context = {
            'locals':locals,
        }
        return render(request,'users/news.html',context)

def newspoint(request):
    locals = news.local_news()
    return HttpResponse(locals)

class PostDetailView(DetailView):
    model = Post
    template_name = 'mainapp/article.html'

    def post(self,*args,**kwargs):
        user = self.request.user
        if user.is_authenticated:
            comment = self.request.POST['comment']
            post = Post.objects.get(id =self.kwargs.get('pk'))
            obj = Comment.objects.create(
                user = user,
                comment = comment,
                post = post
            )
            obj.save()
            return redirect('news_detail',self.kwargs.get('pk'))
        else:
            messages.info(self.request,'Login for your Opinion to count!')
            return redirect('login')

def UserLikePost(request,pk):
    user = request.user
    if user.is_authenticated:
        post = get_object_or_404(Post, id= request.POST.get('userpost_id'))
        post.likes.add(request.user)
        return HttpResponseRedirect(f'/users/news/{post.id}/detail/')
    else:
        messages.info(request,'Login for your Opinion to count!')
        return HttpResponseRedirect(reverse('login'))

def UserLikecomment(request,pk):
    user = request.user
    if user.is_authenticated:
        post = request.POST.get('userpost_id')
        comment = get_object_or_404(Comment, id = pk)
        print(comment)
        comment.likes.add(user)
        return HttpResponseRedirect(f'/users/news/{post}/detail/')
    else:
        messages.info(request,'Login for your Opinion to count!')
        return HttpResponseRedirect(reverse('login'))  