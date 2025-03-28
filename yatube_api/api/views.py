from rest_framework import permissions, viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from posts.models import Post, Comment, Group, Follow
from .serializers import PostSerializer, CommentSerializer
from .serializers import GroupSerializer, FollowSerializer
from rest_framework.response import Response


class ReadOnlyOrOwner_(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in permissions.SAFE_METHODS


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


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
                        post=Post.objects.get(id=self.kwargs['post_id']))


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (ReadOnly,)


class FollowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request):
        serializer = FollowSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"error": "Неверные данные"}, status=400)

        user = request.user
        target = serializer.validated_data['following']

        if target.username == user.username:
            return Response(
                {"error": "Нельзя подписаться на самого себя."},
                status=400
            )

        if Follow.objects.filter(user=user, following=target).exists():
            return Response(
                {"error": "Подписка уже существует"},
                status=400
            )

        serializer.save(user=user, following=target)
        return Response(serializer.data, status=201)
