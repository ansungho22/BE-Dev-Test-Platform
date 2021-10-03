from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("today/<str:city>/", views.Weather.as_view()),
]
