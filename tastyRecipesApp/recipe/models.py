from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from tastyRecipesApp.user.models import Profile


class Recipe(models.Model):
    MAX_RECIPE_LENGTH = 100
    MIN_RECIPE_LENGTH = 10
    MIN_CUISINE_TYPE_LENGTH = 7
    MIN_VALUE_COOKING_TIME = 1
    CUISINE_TYPE_CHOICES = (
        ('french', 'French'),
        ('chinese', 'Chinese'),
        ('italian', 'Italian'),
        ('balkan', 'Balkan'),
        ('other', 'Other'),
    )

    title = models.CharField(
        blank=False, null=False, unique=True,
        max_length=MAX_RECIPE_LENGTH,
        validators=[MinLengthValidator(MIN_RECIPE_LENGTH),],
        error_messages={'unique': "We already have a recipe with the same title!"},
    )
    cuisine_type = models.CharField(
        blank=False, null=False,
        choices=CUISINE_TYPE_CHOICES,
        max_length=MIN_CUISINE_TYPE_LENGTH
    )
    ingredients = models.TextField(
        blank=False, null=False,
        help_text="Ingredients must be separated by a comma and space."
    )
    instructions = models.TextField(
        blank=False, null=False,
    )
    cooking_time = models.PositiveIntegerField(
        blank=False, null=False,
        validators=[MinValueValidator(MIN_VALUE_COOKING_TIME),],
        help_text="Provide the cooking time in minutes."
    )
    image_url = models.URLField(
        blank=True, null=True,
    )
    author = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               related_name='recipes')
