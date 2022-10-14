from urllib.request import Request
from django.shortcuts import render
from django.shortcuts import redirect
from .urls import obtain_token
from asili.models import  Customer

# from wallet.models import Wallet

# Create your views here.

def register_customer(request):

    if request.method == 'POST':
        form =  Customer(request.POST)
        if form.is_valid():
            form.save()
    
    else: 
        form = Customer()

    return render(request, "asili/register_customer.html", {"form": form})


def list_customers(request):
    customers = Customer.objects.all()
    return render (request, 'asili/list_customers.html', {'customers': customers})


def customer_profile(request, id):
    customer = Customer.objects.get(id=id)
    return render (request, 'asili/customer_profile.html', {'customer': customer})
    

def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = Customer(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id=customer.id) 
    else:
        form = Customer(request.POST, instance=customer)
        return render(request,"asili/edit_customer.html",{'form':form})