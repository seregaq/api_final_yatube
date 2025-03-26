from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.urls import reverse
from urllib.parse import urlencode
from posts.models import Post
from api.serializers import PostSerializer
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_query_param = 'offset'
    
    def get_paginated_response(self, data):
        base_url = self.request.build_absolute_uri()
        query_params = self.request.GET.copy()
        
        next_url = None
        if self.page.has_next():
            query_params['offset'] = self.page.next_page_number()
            next_url = f"{base_url}?{urlencode(query_params)}"
        
        previous_url = None
        if self.page.has_previous():
            query_params['offset'] = self.page.previous_page_number()
            previous_url = f"{base_url}?{urlencode(query_params)}"
        
        return Response({
            'count': self.page.paginator.count,
            'next': next_url,
            'previous': previous_url,
            'results': data
        })

@api_view(['GET'])
def get_publications(request):
    # Получаем все публикации (замените на вашу модель)
    publications = Post.objects.all()  # Publication - это пример, замените на вашу модель
    
    paginator = CustomPagination()
    result_page = paginator.paginate_queryset(publications, request)
    
    serializer = PostSerializer(result_page, many=True)   
    
    return paginator.get_paginated_response(serializer.data)
