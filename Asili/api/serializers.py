from calendar import c
from dataclasses import fields
from rest_framework import serializers
from api.models import User
from django.contrib.auth.models import User
from .import models

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ( 'first_name', 'last_name','email','password')

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.User
        fields = ('first_name', 'last_name','email','password')
        extra_kwargs = {'password': {'write_only': True}}
def create(self, validated_data):
    user = models.User.objects.create(validated_data['email'],validated_data['password'],)
    return user