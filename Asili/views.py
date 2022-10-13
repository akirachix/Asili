from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

  
def imageView(request):
  
    if request.method == 'POST':
        form = ClothForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ClothForm()
    return render(request, 'asili/clothform.html', {'form' : form})
  
  
def uploadok(request):
    return HttpResponse(' upload successful')