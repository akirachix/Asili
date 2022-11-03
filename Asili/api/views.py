from email import parser
from lib2to3.pgen2 import token
from django.conf import settings



 
# Create your views here.
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import viewsets
from .models import Categories, Designer, Kids, User, Men, Women
from .serializers import DesignerSerializer, UserSerializer, CategoriesSerializer, MenSerializer, WomenSerializer, KidsSerializer
 

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