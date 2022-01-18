from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    """class utilisateurs"""


class Project(models.Model):
    title = models.fields.CharField(max_length=128)
    description = 
    type = models.fields.CharField(max_length=128)
    author_user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)


class Contributor(models.Model):
    CREATOR = 'CREATOR'
    CONTRIBUTOR = 'CONTRIBUTOR'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (CONTRIBUTOR, 'Contributeur'),
    )
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
    project_id = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='rôle')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creator')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='contributor')
            group.user_set.add(self)



