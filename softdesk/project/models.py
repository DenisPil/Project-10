from django.db import models
from django.conf import settings


class Types(models.TextChoices):
    BACK_END = 'back-end'
    FRONT_END = 'front-end'
    IOS = 'IOS'
    ANDROID = 'Android'


class Project(models.Model):

    """Classe qui représente le model des projets"""

    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048)
    type = models.fields.CharField(choices=Types.choices, max_length=10)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
