from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  balance = models.FloatField('Saldo', default=0)