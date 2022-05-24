from django.urls import path 
from jwt_auth.views import RegisterView, LoginView, CredentialsView, UsersView, UserCollectionView

urlpatterns = [ 
  path('register/', RegisterView.as_view()), 
  path('login/', LoginView.as_view()), 
  path('credentials/', CredentialsView.as_view()),
  path('users/', UsersView.as_view()),
  path('users/<int:pk>', UserCollectionView.as_view()),
  path('users/<int:pk>/collection/', UserCollectionView.as_view())
]