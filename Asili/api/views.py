from email import parser
from lib2to3.pgen2 import token
# from typing_extensions import Self
from django.conf import settings
from django.shortcuts import render
from django.views import View
from requests import Response, request
 
# Create your views here.
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import viewsets
from .models import Categories, Designer, Kids, User, Men, Women
from .serializers import DesignerSerializer, UserSerializer, CategoriesSerializer, MenSerializer, WomenSerializer, KidsSerializer
 

# from django import forms
# from django.http import HttpResponse

# from cloudinary.forms import cl_init_js_callbacks      
# from .models import Photo
# from .forms import PhotoForm

# def upload(request):
#   context = dict( backend_form = PhotoForm())

#   if request.method == 'POST':
#     form = PhotoForm(request.POST, request.FILES)
#     context['posted'] = form.instance
#     if form.is_valid():
#         form.save()

#   return render(request, 'upload.html', context)


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class DesignerViewSet(viewsets.ModelViewSet):
   queryset = Designer.objects.all()
   serializer_class = DesignerSerializer
 
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