from django.contrib import admin
from django.urls import path, include
from backend import views

urlpatterns = [
    path("", views.index, name="home"),
    path('adminApp/', include('adminApp.urls')),
    path('minerApp/', include('minerApp.urls')),
    path("blockchain/", include("backend.urls")),
    path("vote/", include("voterApp.urls")),

    path('admin/', admin.site.urls),
]
