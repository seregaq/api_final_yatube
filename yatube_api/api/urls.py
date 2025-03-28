from django.urls import path, include
from api.views import CommentViewSet, PostViewSet
import djoser
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post-list')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='post-comments')


urlpatterns = [

    path('', include(router.urls))
   
    
]
