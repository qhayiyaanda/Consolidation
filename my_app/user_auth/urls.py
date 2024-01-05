from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.registration, name='register'),
]