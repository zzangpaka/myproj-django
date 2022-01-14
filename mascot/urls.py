from rest_framework.routers import DefaultRouter

from mascot import views
from mascot.views import CharacterViewSet
from django.urls import path, include

app_name = "mascot"

router = DefaultRouter()
router.register("characters", CharacterViewSet)

urlpatterns = [
    path("characters.json", views.character_list),
    path("api/", include(router.urls)),
]