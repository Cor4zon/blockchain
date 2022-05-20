from django.contrib import admin
from django.urls import path, include
from backend import views

app_name = "blockchain"

urlpatterns = [
    path('', views.index, name="home"),
    path('keys', views.new_keys, name="keys"),
    path('result/<int:pk>', views.get_results, name="result"),
]