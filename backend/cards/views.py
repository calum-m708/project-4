from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

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

class CardCreatedByUser(APIView):
  def get(self, request):
    cards = Card.objects.filter(created_by=request.user.id)
    serialized_cards = PopulatedCardSerializer(cards, many=True)
    return Response(serialized_cards.data)