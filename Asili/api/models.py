from email import message
from django.db import models

class Notification(models.Model):
    unique_identifier = models.CharField(max_length=10)
    order_on = models.DateTimeField(auto_now_add=True)
    received_at = models.DateTimeField(auto_now_add=True)
    delivered_on = models.DateTimeField()
    message = models.TextField()

class User(models.Model):
    first_name = models.CharField(max_length=10, null = True)
    last_name = models.CharField(max_length=10, null = True)
    password = models.CharField(max_length=10) 
    profile = models.ImageField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()

class Preferences(models.Model):
    design = models.CharField(max_length=10)
    measurement =models.PositiveSmallIntegerField()
    color = models.CharField(max_length=10, blank=True)
    material = models.CharField(max_length=10, blank=True)
    occasion = models.PositiveSmallIntegerField()

class Bodytype(models.Model):
    plus_size = models.ImageField()
    plump = models.ImageField()
    ptriangle = models.ImageField()

class Categories(models.Model):
    new = models.TextField()
    newarrivals = models.TextField()
    men = models.TextField()
    women = models.TextField()
    kids = models.TextField()
    mostpopular = models.TextField()
    prices = models.CharField(max_length=10)
    brand = models.CharField(max_length=25)
