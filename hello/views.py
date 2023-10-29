from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# I created view so that when user makes a request to a server the HTTP responds with Hello World
# In addition to above, I need to specify what URLs can produce the below response when run
# I can specify this by creating a specific urls.py file for hello which has a list of these possible URLs 

def index(request):
    return HttpResponse("Hello, Christiana!")
    # We used above to render a string, if we do not want to do that we can render a HTML page like below
    # rendering HTML page requires render functionality - parameters are the request and a template to create
  #  return render(request, "hello/index.html")

def ekwulummili(request):
    return HttpResponse("I am from Ekwulummili")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

