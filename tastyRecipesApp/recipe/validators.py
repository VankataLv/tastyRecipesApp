from django.core.exceptions import ValidationError


def validate_title_min_length(value: str):
    if len(value) < 10:
        raise ValidationError("We already have a recipe with the same title!")
