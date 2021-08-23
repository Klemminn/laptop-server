import os
from django.core.exceptions import ValidationError

def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg', '.webp']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Only .jpg, .png and .webp are allowed')
