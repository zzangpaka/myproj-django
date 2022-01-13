from rest_framework import viewsets
from news.serializers import ArticleSerializer
from news.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer