from urllib.request import Request
from django.shortcuts import render
from django.shortcuts import redirect

from wallet.models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Third_party, Transaction, Wallet

# from wallet.models import Wallet

# Create your views here.

def register_customer(request):

    if request.method == 'POST':
        form =  CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    
    else: 
        form = CustomerRegistrationForm()

    return render(request, "wallet/register_customer.html", {"form": form})


def list_customers(request):
    customers = Customer.objects.all()
    return render (request, 'wallet/list_customers.html', {'customers': customers})


def customer_profile(request, id):
    customer = Customer.objects.get(id=id)
    return render (request, 'wallet/customer_profile.html', {'customer': customer})
    

def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id=customer.id) 
    else:
        form = CustomerRegistrationForm(request.POST, instance=customer)
        return render(request,"wallet/edit_customer.html",{'form':form})