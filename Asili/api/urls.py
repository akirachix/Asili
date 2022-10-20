from django.urls import path, include
from rest_framework import routers
from .views import DesignerViewSet, UserViewSet, CategoriesViewSet, MenViewSet, WomenViewSet, KidsViewSet
router = routers.DefaultRouter()
router.register(r"User", UserViewSet)
router.register(r"Designer", DesignerViewSet)
router.register(r"Categories", CategoriesViewSet)
router.register(r"men", MenViewSet)
router.register(r"women", WomenViewSet)
router.register(r"kids", KidsViewSet)


urlpatterns = [
    path("", include(router.urls)),
]