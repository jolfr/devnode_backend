from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User information"""
    user_id = models.CharField(max_length=1024)
    email = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    picture = models.TextField
    given_name = models.CharField(max_length=256)
    family_name = models.CharField(max_length=256)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField

    def __str__(self):
        """Return a string representation of the model"""
        return self.user_id

