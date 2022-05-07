from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from adminApp import views

urlpatterns = [
    path('votings/', views.VotingList.as_view()),
    path('votings/<int:pk>/', views.VotingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
