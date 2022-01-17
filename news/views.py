import json

from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
# from news.serializers import ArticleAnonymousSerializer, ArticleGoldMembershipSerializer, ArticleAdminSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from news.serializers import ArticleSerializer
from news.models import Article
from rest_framework.generics import ListAPIView


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [AllowAny] # DRF 디폴트 설정(누구나)
    permission_classes = [IsAuthenticated] # 인증 된 누구나

    # def get_serializer_class(self):
    #     # return ArticleAnonymousSerializer
    #     # return ArticleGoldMembershipSerializer
    #     return ArticleAdminSerializer
    #
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #
    #     query = self.request.query_params.get("query", "")
    #     if query:
    #         qs = qs.filter(title__icontains=query)
    #
    #     year = self.request.query_params.get("year", "")
    #     if year:
    #         qs = qs.filter(created_at__year=year)
    #
    #     return qs

# article_list = ListAPIView.as_view(
#     queryset=Article.objects.all(),
#     serializer_class=ArticleSerializer,
# )


# step 1
# def article_list(request):
#     qs = Article.objects.all()
#     serializer = ArticleSerializer(qs, many=True)
#     data = serializer.data
#     # data = [
#     #     {
#     #         "id": article.id,
#     #         "title": article.title,
#     #         "content": article.content,
#     #         "photo": request.build_absolute_uri(article.photo.url) if article.photo else None,
#     #     }
#     #     for article in qs
#     # ]
#     json_string = json.dumps(data)
#     return HttpResponse(json_string)