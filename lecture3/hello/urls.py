from django.urls import path
from . import views

# this list will contain all acceptable urls that can be accessed by the app
# we can create url routes for each function (def) on the views.py page

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>", views.greet, name = "greet"),
    path("ekwulummili", views.ekwulummili, name = "ekwulimmili")
    
]