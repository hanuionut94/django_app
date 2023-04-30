from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    cnp = models.CharField(primary_key=True, max_length=13, unique=True, verbose_name='CNP')

# Create your models here.
