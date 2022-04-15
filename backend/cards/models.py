from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=30)
    strength = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    charisma = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    intelligence = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    special = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    image = CloudinaryField('image')
    def __str__(self):
      return self.name
