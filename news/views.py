import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from news.serializers import ArticleSerializer
from news.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [AllowAny] # DRF 디폴트 설정(누구나)
    permission_classes = [IsAuthenticated] # 인증 된 누구나


def article_list(request):
    qs = Article.objects.all()
    data = [
        {
            "id": article.id,
            "title": article.title,
            "content": article.content
        }
        for article in qs
    ]
    json_string = json.dumps(data)
    return HttpResponse(json_string)