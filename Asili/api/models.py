
from sre_constants import CATEGORY
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
 
 
 
CLOTH_TYPE_CHOICES = (("dress","dress"), ("trouser","trouser"),("shirts","shirts"))
# CATEGORY=(("men","men"), ("women","women"),("kids","kids"),("mostpopular","mostpopular"))
WEARER= (("Men","Men"),("Women","Women"), ("Kids","Kids"))
class Categories(models.Model):
    image =  models.ImageField(upload_to='pictures/')
    type = models.CharField(max_length= 10,choices=CLOTH_TYPE_CHOICES, null = True )
    wearer = models.CharField(max_length= 10,choices=WEARER, null = True ,default='SOME STRING')
    def __str__(self):
        return self.wearer
 
class Men(models.Model):
   image =  models.ImageField(upload_to='pictures/')
   type = models.CharField(max_length= 10,choices=CLOTH_TYPE_CHOICES, null = True )
   wearer = models.CharField(max_length= 10,choices=WEARER, null = True ,default='SOME STRING')
   def __str__(self):
    return self.wearer
 
class Women(models.Model):
  image =  models.ImageField(upload_to='pictures/')
  type = models.CharField(max_length= 10,choices=CLOTH_TYPE_CHOICES, null = True )
  wearer = models.CharField(max_length= 10,choices=WEARER, null = True ,default='SOME STRING')
  def __str__(self):
    return self.wearer
 
class Kids(models.Model):
  image =  models.ImageField(upload_to='pictures/')
  type = models.CharField(max_length= 100,choices=CLOTH_TYPE_CHOICES, null = True )
  wearer = models.CharField(max_length= 10,choices=WEARER, null = True ,default='SOME STRING')
  def __str__(self):
    return self.wearer