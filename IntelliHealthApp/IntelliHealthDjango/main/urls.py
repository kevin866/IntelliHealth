from django.urls import path

from . import views

urlpatterns = [
    path("", views.api_health, name="api_health"),
    path("chat", views.chatgpt, name="chatgpt"),
]