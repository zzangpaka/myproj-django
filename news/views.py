import json

from django.http import HttpResponse
from rest_framework import viewsets
from news.serializers import ArticleSerializer
from news.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


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