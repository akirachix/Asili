from dataclasses import fields
from operator import mod
from rest_framework import serializers
from asili.models import Customer

# Create your models here.

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "age", "email", )