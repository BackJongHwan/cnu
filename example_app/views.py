from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
   return HttpResponse("Hello, World!")

def home(request):
    return HttpResponse("Welcome to the Example App Home Page!")


def about(request):
   return HttpResponse("This is the About Page for the Example App.")


def contact(request):
   return HttpResponse("Contact us at: contact@example.com")