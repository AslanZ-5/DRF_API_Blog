from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('myblog.urls')),
                  path('api/posts/', include('myblog.api.urls',namespace='api-post')),
                  path('users/', include('django.contrib.auth.urls')),
                  path('users/', include('users.urls'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
