from urllib import request
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.

class Match(models.Model):
  player = models.ForeignKey('jwt_auth.CustomUser', related_name='match', on_delete=models.CASCADE)
  date_time = models.DateTimeField(auto_now=True)
  won = models.BooleanField()
  cards_won = models.PositiveSmallIntegerField()


class Card(models.Model):
  name = models.CharField(max_length=30)
  strength = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
  charisma = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
  intelligence = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
  special = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
  image = CloudinaryField('image')
  created_by = models.ForeignKey('jwt_auth.CustomUser', related_name='card', on_delete=models.SET_DEFAULT, default=1)
  def __str__(self):
    return self.name
