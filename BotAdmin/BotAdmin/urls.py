from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('embed/', include("embed.urls")),
    path('user/', include("user.urls")),
    path('tournament/', include("tournament.urls")),
    path('scenario/', include("scenario.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
