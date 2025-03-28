# TODO:  Напишите свой вариант
from rest_framework import generics, permissions, viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from rest_framework import permissions


class ReadOnlyOrOwner_(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in permissions.SAFE_METHODS


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (ReadOnlyOrOwner_,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (ReadOnlyOrOwner_,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
        post = Post.objects.get(id=self.kwargs['post_id']))






