
from sre_constants import CATEGORY
from django.db import models
from .models import CloudinaryField




class User(models.Model):
    
   first_name = models.CharField(max_length=10, null = True)
   last_name = models.CharField(max_length=10, null = True)
   password = models.CharField(max_length=10)
   email = models.EmailField()
 
 
class Designer(models.Model):
   first_name = models.CharField(max_length=10, null = True)
   last_name = models.CharField(max_length=10, null = True)
   password = models.CharField(max_length=10)
   email = models.EmailField()
 
 
 
CLOTH_TYPE_CHOICES = (("skirts","skirts"),("dress","dress"), ("trouser","trouser"),("shirts","shirts"))
# CATEGORY=(("men","men"), ("women","women"),("kids","kids"),("mostpopular","mostpopular"))
WEARER= (("Men","Men"),("Women","Women"), ("Kids","Kids"))

class Categories(models.Model):
    image =  CloudinaryField('pictures')
    type = models.CharField(max_length= 10,choices=CLOTH_TYPE_CHOICES, null = True )
    wearer = models.CharField(max_length= 100,choices=WEARER, null = True ,default='SOME STRING')
    def __str__(self):
        return self.wearer
 
class Men(models.Model):
    image = CloudinaryField('pictures')
    type = models.CharField(max_length= 10,choices=CLOTH_TYPE_CHOICES, null = True )
   #  wearer = models.CharField(max_length= 10,choices=WEARER, null = True ,default='SOME STRING')
    def __str__(self):
        return self.image
 
class Women(models.Model):
    image =  CloudinaryField('pictures')
    type = models.CharField(max_length= 10,choices=CLOTH_TYPE_CHOICES, null = True )
   #  wearer = models.CharField(max_length= 10,choices=WEARER, null = True ,default='SOME STRING')
    def __str__(self):
        return self.image
        
class Kids(models.Model):
    image =CloudinaryField('pictures')
    type = models.CharField(max_length= 10,choices=CLOTH_TYPE_CHOICES, null = True )
   #  wearer = models.CharField(max_length= 10,choices=WEARER, null = True ,default='SOME STRING')
    def __str__(self):
        return self.image