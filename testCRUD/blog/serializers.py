from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from blog.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'registered')


class CommentSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'user', 'created_date')

    def get_user(self, obj):
        return obj.user.name


class PostSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    comments = CommentSerializer(source='comments.text')

    class Meta:
        model = Post
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.name
