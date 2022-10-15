from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from blog.models import *
from blog.serializers import *


class IndexView(APIView):
    def get(self, request):
        return Response({'title': "Главная страница", 'message': 'the site is loaded'})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=['get', 'post'], detail=True)
    def comment(self, request, pk=None):
        if request.method == 'GET':
            comments = Comment.objects.filter(post__pk=pk)
            comments_serializer = CommentSerializer(comments, many=True)
            return Response(comments_serializer.data)
        elif request.method == 'POST':
            comment_serializer = CommentSerializer(data=request.data, many=True)
            comment_serializer.is_valid(raise_exception=True)
            comment_serializer.save()
            return Response(comment_serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Comment.objects.all().reverse()[:10]

        return Comment.objects.filter(pk=pk)