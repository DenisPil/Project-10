from django.db import models

from project.models import Project
from user.models import User


class Types(models.TextChoices):
    CREATOR = 'CREATOR'
    CONTRIBUTOR = 'CONTRIBUTOR'


class Contributor(models.Model):

    """ Classe qui représente le model des contributeurs qui fait le liens entre les utilisateurs et les projects"""

    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributor')
    contributor_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributor_id')
    role = models.CharField(max_length=30, choices=Types.choices, verbose_name='rôle')
