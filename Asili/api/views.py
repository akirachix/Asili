
from email import parser
from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import viewsets
from asili.models import Categories, User, Men, Women, Kids
from .serializers import DesignerSerializer, UserSerializer, CategoriesSerializer, MenSerializer, WomenSerializer, KidsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DesignerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = DesignerSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    parser_classes=(FormParser, MultiPartParser)

class MenViewSet(viewsets.ModelViewSet):
    queryset = Men.objects.all()
    serializer_class = MenSerializer

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class KidsViewSet(viewsets.ModelViewSet):
    queryset = Kids.objects.all()
    serializer_class = KidsSerializer
