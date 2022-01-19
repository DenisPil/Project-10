from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    """class utilisateurs"""
    projects_creator= models.ManyToManyField('Project', through='Contributor')


class Project(models.Model):
    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048)
    type = models.fields.CharField(max_length=128)
    # author_user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
    author_user_id = models.ManyToManyField('User',through='Contributor')


class Contributor(models.Model):
    CREATOR = 'CREATOR'
    CONTRIBUTOR = 'CONTRIBUTOR'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (CONTRIBUTOR, 'Contributeur'),
    )
    creator_id = models.ForeignKey('User', on_delete=models.CASCADE,related_name='creator_id_Contributor')
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE,related_name='project_id_Contributor')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='rôle')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creator')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='contributor')
            group.user_set.add(self)


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
    desc = models.fields.CharField(max_length=2048)
    tag = models.fields.CharField(choices=Tags.choices, max_length=8)
    priority = models.fields.CharField(choices=Priorites.choices, max_length=8)
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE,related_name='project_id_issue')
    status = models.fields.CharField(max_length=64)
    author_user_id = models.ForeignKey('User', on_delete=models.CASCADE,related_name='author_user_id_issue')
    assignee_user_id = models.ForeignKey('User', on_delete=models.CASCADE,related_name='assignee_user_id_issue')
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    
    description = models.fields.CharField(max_length=2048)
    author_user_id = models.ForeignKey('User', on_delete=models.CASCADE,related_name='author_user_id_comment')
    issue_id = models.ForeignKey('Issue', on_delete=models.CASCADE,related_name='issue_id_comment')
    created_time = models.DateTimeField(auto_now_add=True)
