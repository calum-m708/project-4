from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from .models import *
from .serializers.common import *
# Create your views here.

class CardList(ListCreateAPIView):
  queryset = Card.objects.all()
  serializer_class = CardSerializer

class CardUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Card.objects.all()
  serializer_class = CardSerializer

class CardDetail(RetrieveAPIView):
  queryset = Card.objects.all()
  serializer_class = PopulatedCardSerializer