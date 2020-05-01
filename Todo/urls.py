from django.contrib import admin
from django.urls import path
from .views import main, update

app_name = "Todo"
urlpatterns = [
    path("", main, name="main"),
    path("update", update, name="update"),
]
