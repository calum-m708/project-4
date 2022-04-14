from django.db import models

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=30)
    strength = models.IntegerField()
    charisma = models.IntegerField()
    intelligence = models.IntegerField()
    special = models.IntegerField()
    image = models.CharField(max_length=300)
