# TODO:  Напишите свой вариант
from rest_framework import generics, permissions, viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = ()
    pagination_class = LimitOffsetPagination
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

