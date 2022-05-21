from django.urls import path
from minerApp import views

urlpatterns = [
    path('mine', views.mine, name="mine"),
]
