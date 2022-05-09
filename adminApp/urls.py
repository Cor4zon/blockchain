from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from adminApp import views

urlpatterns = [
    path('votings/', views.VotingList.as_view()),
    path('votings/<int:pk>/', views.VotingDetail.as_view()),
    path('voters/', views.VoterList.as_view()),
    path('voters/<int:pk>/', views.VoterDetail.as_view()),
    path('voting_options/', views.VotingOptionList.as_view()),
    path('voting_options/<int:pk>/', views.VotingOptionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
