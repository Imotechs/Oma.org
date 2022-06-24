from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView
from mainapp.models import Album, Artist,Song,ArtistSong,Event
from users.forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.conf import settings

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