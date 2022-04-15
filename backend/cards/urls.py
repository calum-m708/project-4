from django.urls import path
from cards.views import *
urlpatterns = [
  path('cards/', CardList.as_view())
]