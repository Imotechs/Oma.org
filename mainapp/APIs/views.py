from rest_framework import mixins,generics
from rest_framework.views import APIView
from mainapp.models import Song
from django.shortcuts import get_object_or_404, redirect
from mainapp.serializers import SongSerializer,PostSerializer
from rest_framework.response import Response
from users.models import Post
#CRUD
class SongsApiView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView,
    ):
    serializer_class = SongSerializer
    permission_classes = []
    authentication_classes = []
    
    def get_queryset(self):
        request = self.request
        qs = Song.objects.all()
        query = request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(title__icontains = query)
        return qs

    def get_object(self):
        request = self.request
        id = request.GET.get('id',None)
        query = self.get_queryset()
        obj = None
        if id is not None:
            obj = get_object_or_404(query,id = id)
            self.check_object_permissions(request,obj)
        return obj
    def get(self,request,*args,**kwargs):
        id = self.request.GET.get('id',None)
        if id:
            return self.retrieve(request,*args,*kwargs)
        return super().get(request,*args,**kwargs) 
        
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class PostApiView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView,
    ):
    serializer_class = PostSerializer
    permission_classes = []
    authentication_classes = []
    
    def get_queryset(self):
        request = self.request
        qs = Post.objects.all()
        query = request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(title__icontains = query)
        return qs

    def get_object(self):
        request = self.request
        id = request.GET.get('id',None)
        query = self.get_queryset()
        obj = None
        if id is not None:
            obj = get_object_or_404(query,id = id)
            self.check_object_permissions(request,obj)
        return obj
    def get(self,request,*args,**kwargs):
        id = self.request.GET.get('id',None)
        if id:
            return self.retrieve(request,*args,*kwargs)
        return super().get(request,*args,**kwargs) 
        
    def post(self,request,*args,**kwargs):
        self.create(request,*args,**kwargs)
        return redirect('dashboard')
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        self.delete(request,*args,**kwargs)
        return redirect('/')
