from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model
from posts.models import Comment, Post, Group, Follow 

User = User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'post')

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group

class FollowSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField (
            slug_field = 'username',
            read_only = True
    )
    following = serializers.SlugRelatedField(
            slug_field = 'username',
            queryset = User.objects.all()

    )
    
    class Meta:
        fields = ('user', 'following')
        model = Follow
        read_only_fields = ('user',)
        
        


