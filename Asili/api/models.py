
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class User(models.Model):

    first_name = models.CharField(max_length=10, null = True)
    last_name = models.CharField(max_length=10, null = True)
    password = models.CharField(max_length=10) 
    profile = models.ImageField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)

class Designer(models.Model):
    first_name = models.CharField(max_length=10, null = True)
    last_name = models.CharField(max_length=10, null = True)
    password = models.CharField(max_length=10) 
    profile = models.ImageField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
   



class Categories(models.Model):
    new = models.ImageField(upload_to="pictures/")
    men = models.ImageField(upload_to="pictures/")
    women = models.ImageField(upload_to="pictures/")
    kids = models.ImageField(upload_to="pictures/")
    mostpopular = models.ImageField(upload_to="pictures/")
    

class Men(models.Model):
    trousers = models.ImageField(upload_to="pictures/")
    shirts = models.ImageField(upload_to="pictures/")
    jackets = models.ImageField(upload_to="pictures/")
    suits = models.ImageField(upload_to="pictures/")

class Women(models.Model):
    trousers = models.ImageField(upload_to="pictures/")
    shirts = models.ImageField(upload_to="pictures/")
    jackets = models.ImageField(upload_to="pictures/")
    dress = models.ImageField(upload_to="pictures/")
    skirts = models.ImageField(upload_to="pictures/")

class Kids(models.Model):
    trousers = models.ImageField(upload_to="pictures/")
    shirts = models.ImageField(upload_to="pictures/")
    jackets = models.ImageField(upload_to="pictures/")
    dress = models.ImageField(upload_to="pictures/")
    suits = models.ImageField(upload_to="pictures/")


