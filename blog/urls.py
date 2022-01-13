from rest_framework.routers import DefaultRouter

from blog import views
from blog.views import PostViewSet
from django.urls import path, include

app_name = "blog"

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("post.json", views.post_list),
    path("api/", include(router.urls)),
]