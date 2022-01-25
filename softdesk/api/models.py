from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings


class User(AbstractUser):
    """class utilisateurs"""


class Project(models.Model):
    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048)
    type = models.fields.CharField(max_length=128)
    contributor = models.ManyToManyField('User',through='Contributor',
        related_name='+') #through_fields=('project_id',"contributor_id")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Contributor(models.Model):
    CREATOR = 'CREATOR'
    CONTRIBUTOR = 'CONTRIBUTOR'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (CONTRIBUTOR, 'Contributeur'),)
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE,related_name='project_id')
    contributor_id = models.ForeignKey('User', on_delete=models.CASCADE,related_name='contributor_id')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='rôle')


class Issue(models.Model):

    class Tags(models.TextChoices):
        BUG = 'BUG'
        UPGRADE = 'UPGRADE'
        TASK = 'TASK'

    class Priorites(models.TextChoices):
        LOW = 'LOW'
        MEDIUM = 'MEDIUM'
        HIGHT = 'HIGHT'

    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048)
    tag = models.fields.CharField(choices=Tags.choices, max_length=8)
    priority = models.fields.CharField(choices=Priorites.choices, max_length=8)
    project_id = models.ForeignKey('Project',
                                   on_delete=models.CASCADE,
                                   related_name='issue_id_for_project',
                                   null=True)
    status = models.fields.CharField(max_length=64)
    creator = models.ForeignKey('User',
                                       on_delete=models.CASCADE,
                                       related_name='author_user_id_issue')
    assignee_user_id = models.ForeignKey('User',
                                         on_delete=models.CASCADE,
                                         related_name='assignee_user_id_issue')
    created_time = models.DateTimeField(auto_now_add=True)


class Com(models.Model):
    
    description = models.fields.CharField(max_length=2048)
    creator = models.ForeignKey('User',
                                       on_delete=models.CASCADE,
                                       related_name='author_user_id_comment')
    issue_id = models.ForeignKey('Issue',
                                 on_delete=models.CASCADE,
                                 related_name='comment_id_for_issue')
    created_time = models.DateTimeField(auto_now_add=True)
