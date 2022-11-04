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
      if request.method == 'POST':
         form =  User(request.POST)
         if form.is_valid():
            form.save()
         else:
            form = User()
      return render(request, "api/register_customer.html", {"form": form})

class DesignerViewSet(viewsets.ModelViewSet):
   queryset = Designer.objects.all()
   serializer_class = DesignerSerializer

   def register_Designer(request):
      if request.method == 'POST':
         form =  Designer(request.POST)
         if form.is_valid():
            form.save()
         else:
            form = Designer()
      return render(request, "api/register_customer.html", {"form": form})
 
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