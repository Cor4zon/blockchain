from django.contrib import admin
from django.urls import path, include
from backend import views

app_name = "blockchain"

urlpatterns = [
    path('', views.index, name="home"),

]