from django.core.exceptions import ValidationError


def validate_nickname_min_length(value: str):
    if len(value) < 2:
        raise ValidationError("Nickname must be at least 2 chars long!")


def validate_name_capitalized(value: str):
    if not value[0].isupper():
        raise ValidationError("Name must start with a capital letter!")

