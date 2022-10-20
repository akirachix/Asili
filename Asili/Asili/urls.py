
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include('api.urls')),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('docs', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
