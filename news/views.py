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
    # permission_classes = [IsAuthenticated] # 인증 된 누구나

    def get_permissions(self):
        # if self.request.method in ("POST", "PUT", "PATCH", "DELETE"): # 방법 1)
        # 방법 2)
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    # 유효성 검사가 끝나고 나서 실제 serializer.save()를 할 때 수행되는 함수
    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않음
        # 대신 키워드 인자를 통한 속성 지정을 지원함(필드 추가는 콤마(,)로)
        serializer.save(author=self.request.user)