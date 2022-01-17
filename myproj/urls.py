from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('blog/', include("blog.urls")),
    path('mascot/', include("mascot.urls")),
    path('news/', include("news.urls")),
    path('shop/', include("shop.urls")),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)