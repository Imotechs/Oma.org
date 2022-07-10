from django.urls import path,include
from .views import SongsApiView,PostApiView
urlpatterns = [
    path('songs/',SongsApiView.as_view()),
    path('news/point/',PostApiView.as_view(), name = 'postApi')


]