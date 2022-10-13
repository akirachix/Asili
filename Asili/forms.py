from django import forms
from api.models import *
  
class ClothForm(forms.ModelForm):
  
    class Meta:
        model = Cloth
        fields = ['type', 'image','gender']