from django.urls import path
from django.views import View
from .views import (Dashboard,AllUsers,
SongUpdateView,Emails,AllEvents,NewReleaseUpdateView
)
urlpatterns = [
    path('main/', Dashboard.as_view(), name='dashboard'),
    # path('staffs/', Staffs.as_view(), name = 'staffs'),  
    path('all/users/', AllUsers.as_view(), name = 'allusers'),

    path('update/<int:pk>/song/',SongUpdateView.as_view(), name = 'updatesong'),
    path('update/<int:pk>/',NewReleaseUpdateView.as_view(),name ='updatenewrelease'),

    path('all/mails/', Emails.as_view(), name = 'mails'),
    path('all/allevents/',AllEvents.as_view(), name = 'allevents'),

]

#     path('current/deposits/', AllDeposit.as_view(), name = 'deposits'),
#     path('current/withdrawals/', AllWithdraws.as_view(), name = 'withdraws'),
#     path('all/mails/', Emails.as_view(), name = 'mails'),
#     path('send/mails/', MakeMail.as_view(), name = 'sendmails'),
#     path('view/<int:pk>/mails/', ViewEmails.as_view(), name = 'readmail'),
#     path('view/active/trades/', ActiveTrades.as_view(), name = 'activetrades'),
#     path('view/succesfull/trades/', SuccessfulTrades.as_view(), name = 'successfultrades'),
#     path('uploads/views/', AdminUploadView.as_view(), name = 'evidenceview')
#     # path('get/pin/', Pin.as_view(), name = 'pin'),
#     # path('pin/detail/<int:pk>/', PinDetail.as_view(), name = 'pindetails'),
#     # path('pin/payments/', PintPayments.as_view(), name = 'pinpayments'),

# ]
