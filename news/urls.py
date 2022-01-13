from rest_framework.routers import DefaultRouter

from news import views
from news.views import ArticleViewSet
from django.urls import path, include

app_name = "news"

router = DefaultRouter()
router.register("articles", ArticleViewSet)

urlpatterns = [
    path("articles.json", views.article_list),
    path("api/", include(router.urls)),
]