from django.urls import path,include
from Asili.views import imageView, uploadok
from rest_framework import routers
from .views import CategoryViewsets, UserViewsets, ClothViewsets
from django.conf import settings
from django.conf.urls.static import static
from .views import *



router = routers.DefaultRouter()
router.register(r'user',UserViewsets)
router.register(r'category',CategoryViewsets)
router.register(r'cloth',ClothViewsets)


urlpatterns = [
    path('',include(router.urls)),
    path('image/', imageView, name = 'image upload'),
    path('success/', uploadok, name = 'success'),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)