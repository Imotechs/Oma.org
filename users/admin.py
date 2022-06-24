from django.contrib import admin
from users.models import  AlbumPayment,EventPayment
# Register your models here.
admin.site.register(AlbumPayment)
admin.site.register(EventPayment)