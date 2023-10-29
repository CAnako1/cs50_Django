from django.urls import path
from . import views

# I added app_name variable so program can differentiate betwwen the name = index which also exists in the new year app

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]