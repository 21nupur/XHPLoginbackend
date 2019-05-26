from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    phone = models.IntegerField()
    address = models.CharField(max_length=255, default='Bihar')

    REQUIRED_FIELDS = ['date_of_birth', 'phone', 'email']