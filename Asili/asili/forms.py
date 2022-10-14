# from xml.parsers.expat import model
from xml.parsers.expat import model
from django import forms
from .models import Card, Customer, Notification,Third_party,Transaction, Wallet, Account, Receipt, Loan, Reward, Currency

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"