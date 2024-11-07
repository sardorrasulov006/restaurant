from django.core.exceptions import ValidationError
import re

def validate_phone_number(phone_number):
    pattern = r'^\+998\d{9}$'  # +998 bilan boshlanib, 9 ta raqam bilan davom etishi kerak
    if not re.match(pattern, phone_number):
        raise ValidationError("Phone number must be in the format +998XXXXXXXXX")
