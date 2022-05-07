from django.contrib import admin
from django.urls import path, include
from backend import views

urlpatterns = [
    path("", views.index, name="home"),
    path('adminApp/', include('adminApp.urls')),
    path("blockchain/", include("backend.urls")),

    path('admin/', admin.site.urls),
]
