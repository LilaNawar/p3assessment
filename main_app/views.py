from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
    return render(request, 'cats/index.html', { 'cats': cats})