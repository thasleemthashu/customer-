from django.core.exceptions import ValidationError
import re


def validate_first_name(value):
    first_name = str(value)
    if not re.match("^[A-Za-z]*$", first_name):
        raise ValidationError("Enter a valid first name")
    return value

def validate_last_name(value):
    last_name = str(value)
    if not re.match("^[A-Za-z]*$", last_name):
        raise ValidationError("Enter a valid last name")
    return value

def validate_age(value):
    age = str(value)
    if not re.match("^[0-9]*$", age):
        raise ValidationError("Enter a Valid age")
    return value

def validate_mobile_no(value):
    mobile_no = str(value)
    if not re.match("^[0-9]*$", mobile_no):
        raise ValidationError("Enter a Valid mobile_no")
    return value


def validate_phone_no(value):
    phone_no = str(value)
    if not re.match("^[0-9]*$", phone_no):
        raise ValidationError("Enter a Valid phone_no")
    return value

def validate_city(value):
    city = str(value)
    if not re.match("^[A-Za-z]*$", city):
        raise ValidationError("Enter a Valid city name")
    return value

def validate_state(value):
    state = str(value)
    if not re.match("^[A-Za-z]*$", state):
        raise ValidationError("Enter a Valid state name")
    return value

def validate_landmark(value):
    landmark = str(value)
    if not re.match("^[A-Za-z]*$", landmark):
        raise ValidationError("Enter a Valid landmark")
    return value

def validate_pincode(value):
    pincode = str(value)
    if not re.match("^[0-9]*$", pincode):
        raise ValidationError("Enter a Valid pincode")
    return value

