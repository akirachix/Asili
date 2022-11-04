from email import parser
from lib2to3.pgen2 import token
# from typing_extensions import Self
from django.conf import settings
from django.shortcuts import render,redirect
from django.views import View
from requests import Response, request
 
# Create your views here.
from rest_framework import viewsets
from .models import Categories, Designer, Kids, User, Men, Women
from .serializers import DesignerSerializer, UserSerializer, CategoriesSerializer, MenSerializer, WomenSerializer, KidsSerializer
 

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

   def register_customer(request):
      if request.method == "POST":
         serializer = UserSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
         return Response(serializer.data, status=201)   

class DesignerViewSet(viewsets.ModelViewSet):
   queryset = Designer.objects.all()
   serializer_class = DesignerSerializer

   def register_customer(request):
      if request.method == "POST":
         serializer = DesignerSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
         return Response(serializer.data, status=201)  
 
class CategoryViewSets(viewsets.ModelViewSet):
   queryset = Categories.objects.all()
   serializer_class = CategoriesSerializer
 
class MenViewSet(viewsets.ModelViewSet):
   queryset = Men.objects.all()
   serializer_class = MenSerializer
 
class WomenViewSet(viewsets.ModelViewSet):
   queryset = Women.objects.all()
   serializer_class = WomenSerializer
 
class KidsViewSet(viewsets.ModelViewSet):
   queryset = Kids.objects.all()
   serializer_class = KidsSerializer