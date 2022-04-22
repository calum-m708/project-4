from rest_framework import serializers
from ..models import *
from jwt_auth.serializers import UserSerializer, CustomUserSerializer

class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    fields = '__all__'


class PopulatedCardSerializer(CardSerializer):
  created_by = CustomUserSerializer()

class MatchSerializer(serializers.ModelSerializer):
  class Meta:
    model = Match
    fields = '__all__'