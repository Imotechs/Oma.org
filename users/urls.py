from django.urls import path
from users.views import register,CreateAlbum,ArtistAddSongView,about
from users.payment import (FlutterPayView,payment_checkout,
PaymentSuccess,event_payment_checkout,EventFlutterPayView,EventPaymentSuccess
)
urlpatterns = [
path('signup/', register, name = 'register'),
path('add/album/', CreateAlbum.as_view(), name = 'addalbum'),
path('add/song/<int:pk>/', ArtistAddSongView.as_view(), name = 'addsong'),
path('about/us/', about, name = 'about'),

# Album payment gateway
path('checkout/<int:pk>/',payment_checkout, name = 'checkout'),
path('make/payment/<int:pk>/',FlutterPayView.as_view(), name = 'payment'),
path('payment/success/',PaymentSuccess.as_view(), name = 'paymentsuccess'),
#end album payment gateway
path('buy/ticket/<int:pk>/',event_payment_checkout, name = 'buyticket'),
path('012/012/payment/event/<int:pk>/aztas/',EventFlutterPayView.as_view(),name ='eventpayment'),
path('012/event/012//payment/success/',EventPaymentSuccess.as_view(), name = 'eventpaymentsuccess'),


]
