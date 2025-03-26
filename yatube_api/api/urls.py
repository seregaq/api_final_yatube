from django.urls import path, include
from api.views import PostListView, PostCreateView
from api.views import PostDetailView, CommentListView
import djoser

urlpatterns = [

    path('api/v1/posts/', PostListView.as_view(), name='post-list'),
    path('api/v1/posts/create/', PostCreateView.as_view(), name='post-create'),
    path('api/v1/posts/<int:pk>/',
          PostDetailView.as_view(), name='post-detail'),
    path('api/v1/posts/<int:post_id>/comments/',
         CommentListView.as_view(), name='post-comments'),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
]
