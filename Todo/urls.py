from django.contrib import admin
from django.urls import path
from .views import main, create, update, delete

app_name = "Todo"
urlpatterns = [
    path("", main, name="main"),
    path("create", create, name="create"),
    path("update", update, name="update"),
    path("delete", delete, name="delete"),
]
