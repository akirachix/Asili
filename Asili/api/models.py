from distutils.command.upload import upload
from django.db import models

# Create your models here.

class User(models.Model):

    first_name = models.CharField(max_length=10, null = True)
    last_name = models.CharField(max_length=10, null = True)
    password = models.CharField(max_length=10) 
    email = models.EmailField()
  

class Designer(models.Model):

    first_name = models.CharField(max_length=10, null = True)
    last_name = models.CharField(max_length=10, null = True)
    password = models.CharField(max_length=10) 
    # profile = models.ImageField()
    email = models.EmailField()
    # gender = models.CharField(max_length=10)




class Categories(models.Model):
    new = models.ImageField(upload_to="pictures/")
    men = models.ImageField(upload_to="pictures/")
    women = models.ImageField(upload_to="pictures/")
    kids = models.ImageField(upload_to="pictures/")
    mostpopular = models.ImageField(upload_to="pictures/")
    

class Men(models.Model):
    trousers = models.ImageField()
    shirts = models.ImageField()
    jackets = models.ImageField()
    suits = models.ImageField()

class Women(models.Model):
    trousers = models.ImageField()
    shirts = models.ImageField()
    jackets = models.ImageField()
    dress = models.ImageField()
    skirts = models.ImageField()

class Kids(models.Model):
    trousers = models.ImageField()
    shirts = models.ImageField()
    jackets = models.ImageField()
    dress = models.ImageField()
    suits = models.ImageField()


