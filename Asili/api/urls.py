from django.urls import path,include
# from api.views import imageView, upload
from rest_framework import routers
from .views import CategoryViewsets, UserViewsets, ClothViewsets
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register(r'user',UserViewsets)
router.register(r'category',CategoryViewsets)
router.register(r'cloth',ClothViewsets)

urlpatterns = [
    path('',include(router.urls)),
]