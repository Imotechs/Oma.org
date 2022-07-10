from django.contrib import admin
from users.models import  AlbumPayment,EventPayment,Account,Withdrowal,Comment,Post
# Register your models here.
admin.site.register(AlbumPayment)
admin.site.register(EventPayment)
admin.site.register(Account)
admin.site.register(Withdrowal)
admin.site.register(Post)
admin.site.register(Comment)