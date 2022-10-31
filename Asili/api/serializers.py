 
from .models import  Designer, User, Categories, Men, Women, Kids
from rest_framework import serializers
 
class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ("id","first_name", "last_name", "email", "password")


class DesignerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Designer
       fields = ("id","first_name", "last_name", "email", "password")
 
 
class CategoriesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Categories
       fields = ("id","image", "type", "wearer")
 
      
 
class MenSerializer(serializers.ModelSerializer):
   class Meta:
       model = Men
       fields = ("id","image", "type")
 
class WomenSerializer(serializers.ModelSerializer):
   class Meta:
       model = Women
       fields = ("id","image", "type")
  
class KidsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Kids
       fields = ("id","image", "type")
 
 
