
from .models import  Cloth, User, Categories
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name','email','password')
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ( 'men', 'women','kids')
class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = ( 'id','image', 'type','gender')