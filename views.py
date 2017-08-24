from django.shortcuts import render
from.forms import CustomerForm
from.forms import AddressForm


def index(request):
    forms = CustomerForm()

   context = {
        "mycustomerform":forms,

   }
    return render(request, "agent/index.html", context)


def address(request):
    form = AddressForm()

   context = {
        "myaddressform":form,
    }
    return  render(request, "agent/address.html", context)