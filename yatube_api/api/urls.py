from django.urls import path, include
from api.views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet
import djoser
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post-list')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='post-comments')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [

    path('', include(router.urls))
   
    
]
