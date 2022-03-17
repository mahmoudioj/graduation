from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("company/", views.Company),
    path("material/", views.Material),
]
