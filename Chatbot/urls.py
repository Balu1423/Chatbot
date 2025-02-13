from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # The new index page for username input
    path('chatbot/', views.chatbot, name='chatbot'),  # Chatbot interface
    path('send_message/', views.send_message, name='send_message'),  # Handle message sending
]
