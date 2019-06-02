from django.contrib.auth.models import User
from rest_framework import serializers
from base.models import Post



class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username') 
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'author', )


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
