from django.urls import path
from . import views

urlpatterns = [
    path("", views.getData),
    path("add/", views.createItem),
    path("register/", views.register, name="register"),
]
