from rest_framework.routers import DefaultRouter
from news.views import ArticleViewSet
from django.urls import path, include

app_name = "news"

router = DefaultRouter()
router.register("articles", ArticleViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]