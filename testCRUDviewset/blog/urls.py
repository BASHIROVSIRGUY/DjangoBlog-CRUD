from django.urls import path, include
from blog.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'post', PostViewSet, basename='post')
router.register(r'comment', CommentViewSet, basename='comment')

# router_comments = routers.SimpleRouter()
# router_comments.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('blog/post/{post_id}/', include(router_comments.urls))
]
