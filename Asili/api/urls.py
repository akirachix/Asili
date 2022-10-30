from django.urls import path,include
# from api.views import imageView, upload
from rest_framework import routers
from .views import CategoryViewSets, UserViewSet,DesignerViewSet,WomenViewSet,MenViewSet,KidsViewSet
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register(r'User',UserViewSet)
router.register(r'Designer',DesignerViewSet)
router.register(r'Category',CategoryViewSets)
router.register(r'Women',WomenViewSet)
router.register(r'Men',MenViewSet)
router.register(r'Kids',KidsViewSet)

urlpatterns = [
    path('',include(router.urls)),
]