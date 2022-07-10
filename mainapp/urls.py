from django.urls import path,include
from .views import (home,profile,artists,
release,events,news,about
,terms,contact,Realese,artistdetail,
AlbumDetail,SongDetail,ShowSongDetail,EventDetail,albums,
SongDownloadView,freealbum,Paidalbum,
NewReleaseDownloadView,NewReleaseDetail,becomeartist,
passreset,post_event
)

import users.views as user_views
urlpatterns = [
    path('', home, name = 'home'),
    path('docs/',include('mainapp.APIs.urls') ),
    path('accounts/login/', user_views.login, name = 'login'),
    path('all/songs/', user_views.Allsongs, name = 'all_songs'),
    path('all_new/release',user_views.Allreleaase,name = 'all_new_release'),
    path('album/<int:pk>/detail', AlbumDetail.as_view(), name = 'albumdetail'),
    path('accounts/profile/', profile, name = 'profile'),
    path('all/artists/', artists, name = 'artists'),
    path('artist/detail/<int:pk>/', artistdetail, name = 'artistdetail'),
    path('all/new/release/', release, name = 'release'),
    path('all/events/', events, name = 'events'),
    path('news/news/', news, name = 'news'),
    path('our/terms/', terms, name = 'terms'),
    path('about/Omaplay/', about, name = 'about'),
    path('contact/Omaplay/', contact, name = 'contact'),
    path('<int:pk>/release/', Realese.as_view(),name = 'releasedetails'),
    path('all/albums/', albums, name = 'albums'),
    path('event/<int:pk>/detail/', EventDetail.as_view(), name = 'eventdetail'),

    path('song/detail/<int:pk>/', SongDetail.as_view(), name = 'songdetail'),
    path('new/song/single/<int:pk>/',ShowSongDetail.as_view(), name = 'showdetail'),
    path('new/release/<int:pk>/', NewReleaseDetail.as_view(), name = 'newreleasedetail'),

    #album
    # path('creat/album/',CreateAlbum.as_view(), name = 'createalbum'),

    path('songs/download/<int:pk>/view/',SongDownloadView.as_view(), name = 'topdownload'),
    # path('songs/download/<int:pk>/new/release',NewReleaseDownloadView.as_view(), name = 'newdownload'),
    path('songs/download/<int:pk>/free/', freealbum, name = 'freealbum'),
    path('songs/downoad/<int:pk>/paid/',Paidalbum, name = 'paidalbum' ),
    path('become/artist/', becomeartist, name = 'becomeartist'),
    path('password/reset/',passreset, name = 'passreset'),
    path('make/event/',post_event, name = 'postevent'),
]
