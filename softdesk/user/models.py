from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """classe qui représente le model des utilisateurs"""
