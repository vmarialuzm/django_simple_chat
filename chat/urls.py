from django.urls import path
from . import views

urlpatterns = [
    path('room/<int:channel_id>/', views.chat_room, name='chat_room'),
    path('create/<int:user_id>/', views.create_channel, name='create_channel')
]