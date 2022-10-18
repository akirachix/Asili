from rest_framework import serializers
from api.models import User
from django.contrib.auth.models import User
from .models import  Category, User, Cloth

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name','email','password')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ( 'men', 'women','kids')

class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = ( 'id','image', 'type','gender')

