from django.urls import path
from adminApp import views

urlpatterns = [
    path('votings/', views.voting_list),
    path('votings/<int:pk>/', views.voting_detail),
]