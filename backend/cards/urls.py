from django.urls import path
from cards.views import *
urlpatterns = [
  path('cards/', CardList.as_view()),
  path('cards/<int:pk>/', CardUpdateDestroy.as_view()),
  path('cards/detail/<int:pk>/',CardDetail.as_view()),
  path('cards/created/',CardCreatedByUser.as_view()),
]