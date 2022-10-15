from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from blog.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'user', 'created_date')

    def get_user(self, obj):
        return obj.user.name


class PostSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'text',
                  'updated_date',
                  'user',
                  'comment_set')

    def get_user(self, obj):
        return obj.user.name
