from rest_framework import serializers
from .models import Song
from users.models import Post

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            'title',
            'artist',
            'genre',
            'audio_file',
            'uploaded_on',

        ]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'description',
            'image',
            'source',
            'uploaded_on',

        ]