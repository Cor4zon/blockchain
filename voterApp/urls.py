from django.urls import path
from voterApp import views

urlpatterns = [
    path('', views.vote, name="vote"),
]
