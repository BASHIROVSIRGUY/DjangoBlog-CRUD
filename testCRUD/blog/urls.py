from django.urls import path
from blog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('user/<int:user_id>/', user_processing_by_id, name='user'),
    path('user/', user_processing, name='users'),
    path('post/<int:post_id>/', post_processing_by_id, name='post'),
    path('post/', post_processing, name='posts'),
    path('comment/<int:comment_id>/', comment_processing_by_id, name='comment'),
    path('post/<int:post_id>/comment/', post_comments_processing, name='post_comments'),
]
