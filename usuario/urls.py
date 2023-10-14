from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from .views import RegisterView
from . import views

urlpatterns = [
    path('account/login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_then_login, name='logout'),
    path('hola/', views.index, name="index")
]