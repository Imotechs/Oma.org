from django.urls import path
from users.views import (
    register,CreateAlbum,
    ArtistAddSongView,about,
    AddReleaseView,AddSongView,
    AddshowSongView,AddGenreView,
    Allsongs,WithDraw,my_events,UserEventDetail,UserAlbumDetail,
    my_news,newspoint,PostDetailView,UserLikePost,UserLikecomment
)
from users.payment import (AlbumPayView,payment_checkout,
PaymentSuccess,event_payment_checkout,EventPayView,EventPaymentSuccess
)
urlpatterns = [
path('signup/', register, name = 'register'),
path('add/album/', CreateAlbum.as_view(), name = 'addalbum'),
path('artist/add/song/<int:pk>/', ArtistAddSongView.as_view(), name = 'addsong'),
path('about/us/', about, name = 'about'),
#add songs route
path('add/song/', AddSongView.as_view(), name = 'addtopsong'),
path('add/show/song/', AddshowSongView.as_view(), name = 'addshowsong'),
path('add/new_released/song/', AddReleaseView.as_view(), name = 'addrelease'),
path('add/genre/', AddGenreView.as_view(), name = 'addgenre'),
path('my/events/',my_events,name = 'my_events'),
path('my/event/<int:pk>/',UserEventDetail.as_view(), name = 'my_event_detail'),
path('my/album/<int:pk>/', UserAlbumDetail.as_view(), name = 'my_album_detail'),
#withdawals
path('withdraw/income/',WithDraw.as_view(), name = 'withdraw'),
# Album payment gateway
path('checkout/<int:pk>/',payment_checkout, name = 'checkout'),
path('make/payment/<int:pk>/',AlbumPayView.as_view(), name = 'payment'),
path('payment/success/<str:ref>/',PaymentSuccess.as_view(), name = 'paymentsuccess'),
#end album payment gateway
path('buy/ticket/<int:pk>/',event_payment_checkout, name = 'buyticket'),
path('012/012/payment/event/<int:pk>/aztas/',EventPayView.as_view(),name ='eventpayment'),
path('012/event/012/payment/success/<str:ref>/',EventPaymentSuccess.as_view(), name = 'eventpaymentsuccess'),

#news
path('news/',my_news, name = 'my_news'),
path('news/point/',newspoint, name = 'newspoint'),
path('news/<int:pk>/detail/',PostDetailView.as_view(), name = 'news_detail'),
path('news/like/<int:pk>/',UserLikePost, name = 'like'),
path('news/like/<int:pk>/',UserLikecomment, name = 'likecomment'),
]
