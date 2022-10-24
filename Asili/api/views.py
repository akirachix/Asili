
from rest_framework import viewsets
from django.shortcuts import render,redirect
# from imageapp.models import GetImage
from .models import Category, User, Cloth
from api.serializers import CategorySerializer, UserSerializer, ClothSerializer

class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class ClothViewsets(viewsets.ModelViewSet):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
# Create your views here.