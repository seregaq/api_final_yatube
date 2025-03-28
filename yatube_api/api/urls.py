from django.urls import path, include
from api.views import PostDetailView, CommentListView, PostViewSet
import djoser
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='route')


urlpatterns = [

    path('', include(router.urls), name='post-list')
   
    
]
