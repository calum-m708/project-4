from django.urls import path 
from jwt_auth.views import RegisterView, LoginView, CredentialsView 

urlpatterns = [ 
  path('register/', RegisterView.as_view()), 
  path('login/', LoginView.as_view()), 
  path('credentials/', CredentialsView.as_view()),
]