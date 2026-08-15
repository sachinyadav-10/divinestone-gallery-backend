from django.urls import path, include
from django.contrib import admin
from divine_main.views import health

urlpatterns = [
    path('health', health),
]