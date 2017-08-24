from django import forms
from .models import Customer
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"