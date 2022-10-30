from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.

class User(models.Model):from django.db import models
# class Notification(models.Model):
#     unique_identifier = models.CharField(max_length=10)
#     order_on = models.DateTimeField(auto_now_add=True)
#     received_at = models.DateTimeField(auto_now_add=True)
#     delivered_on = models.DateTimeField()
#     message = models.TextField()
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
class Category(models.Model):
    new = models.TextField()
    newarrivals = models.TextField()
    men = models.ImageField()
    women = models.ImageField()
    kids = models.ImageField()
    mostpopular = models.TextField()
    prices = models.CharField(max_length=10)
    brand = models.CharField(max_length=25)
CLOTH_TYPE_CHOICES = (("dress","dress"),("suits","suits"), ("trouser","trouser"),("gowns","gowns"))
GENDER_CHOICES = (("Men","Men"),("Women","Women"), ("Kids","Kids"))
class Cloth(models.Model):
    image =  models.ImageField(upload_to='uploads/')
    type = models.CharField(max_length= 10,choices=CLOTH_TYPE_CHOICES, null = True )
    gender = models.CharField(max_length= 10,choices=GENDER_CHOICES, null = True ,default='SOME STRING')
    def __str__(self):
         return self.gender
# Create your models here
  

# class Designer(models.Model):

#     first_name = models.CharField(max_length=10, null = True)
#     last_name = models.CharField(max_length=10, null = True)
#     password = models.CharField(max_length=10) 
#     # profile = models.ImageField()
#     email = models.EmailField()
#     # gender = models.CharField(max_length=10)


# class Categories(models.Model):
#     new = models.ImageField(upload_to="pictures/")
#     men = models.ImageField(upload_to="pictures/")
#     women = models.ImageField(upload_to="pictures/")
#     kids = models.ImageField(upload_to="pictures/")
#     mostpopular = models.ImageField(upload_to="pictures/")
    
# class Men(models.Model):
#     trousers = models.ImageField()
#     shirts = models.ImageField()
#     jackets = models.ImageField()
#     suits = models.ImageField()

# class Women(models.Model):
#     trousers = models.ImageField()
#     shirts = models.ImageField()
#     jackets = models.ImageField()
#     dress = models.ImageField()
#     skirts = models.ImageField()

# class Kids(models.Model):
#     trousers = models.ImageField()
#     shirts = models.ImageField()
#     jackets = models.ImageField()
#     dress = models.ImageField()
#     suits = models.ImageField()


