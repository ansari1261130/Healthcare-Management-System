from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
    def __str__(self):
        return self.username    