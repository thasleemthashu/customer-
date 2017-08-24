from django.db import models
from .validators import *
class ContactInfo(models.Model):
    mobile_no = models.CharField(max_length=15,validators=[validate_mobile_no])
    phone_no = models.CharField(max_length=15, validators=[validate_phone_no])
    email_id = models.EmailField(max_length=50)

class Address(models.Model):
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20, validators=[validate_city])
    state = models.CharField(max_length=20, validators=[validate_state])
    landmark = models.CharField(max_length=50, validators=[validate_landmark])
    pincode = models.CharField(max_length=10, validators=[validate_pincode])

class Customer(ContactInfo):
    cuid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15, validators=[validate_first_name])
    last_name = models.CharField(max_length=15, validators=[validate_last_name])
    age = models.CharField(max_length=2, validators=[validate_age])
    Addresses = models.ManyToManyField("Address")
