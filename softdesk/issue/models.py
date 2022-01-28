from django.db import models

from project.models import Project
from user.models import User
from softdesk.settings import AUTH_USER_MODEL

class Tags(models.TextChoices):
    BUG = 'BUG'
    UPGRADE = 'UPGRADE'
    TASK = 'TASK'


class Priorites(models.TextChoices):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGHT = 'HIGHT'


class Issue(models.Model):

    """ Classe qui représente le model des problémes """

    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048)
    tag = models.fields.CharField(choices=Tags.choices, max_length=8)
    priority = models.fields.CharField(choices=Priorites.choices, max_length=8)
    project_id = models.ForeignKey(Project,
                                   on_delete=models.CASCADE,
                                   related_name='id_issue')
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='author_user_id_issue')
    assignee_user_id = models.ForeignKey(User,
                                         on_delete=models.CASCADE,
                                         related_name='assignee_user_id_issue')
    status = models.fields.CharField(max_length=64)
    created_time = models.DateTimeField(auto_now_add=True)
