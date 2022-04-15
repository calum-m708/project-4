from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView

from .models import *
from .serializers.common import *
# Create your views here.

class CardList(ListCreateAPIView):
  queryset = Card.objects.all()
  serializer_class = CardSerializer