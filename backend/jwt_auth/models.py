from django.db import models
from django.contrib.auth.models import AbstractUser

from cards.models import Card

# Create your models here.

class CustomUser(AbstractUser):
  collection = models.ManyToManyField(Card, related_name="owned_card",default=None)