from django.db import models

from tastyRecipesApp.user.validators import validate_nickname_min_length, \
    validate_name_capitalized


class Profile(models.Model):
    MAX_NICKNAME_LENGTH = 20
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    nickname = models.CharField(
        blank=False, null=False, unique=True,
        max_length=MAX_NICKNAME_LENGTH,
        validators=[validate_nickname_min_length,]
    )
    first_name = models.CharField(
        blank=False, null=False,
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=[validate_name_capitalized,]
    )
    last_name = models.CharField(
        blank=False, null=False,
        max_length=MAX_LAST_NAME_LENGTH,
        validators=[validate_name_capitalized,]
    )
    chef = models.BooleanField(
        blank=False, null=False,
        default=False,
    )
    bio = models.TextField(blank=True, null=True,)
