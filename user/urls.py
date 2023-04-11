from django.urls import path
from . import views

urlpatterns = [
    path('authorization/', views.AuthorizationAPIView.as_view()),
    path('registration/', views.RegistrationAPIView.as_view()),
    path('api/v1/users/confirm/', views.ConfirmUserAPIView.as_view())
]
