from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
# Create your views here.

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# cats = [
#   Cat('Lolo', 'tabby', 'foul little demon', 3),
#   Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]

# /templates/main_app/cat_form.html

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # success_url = '/cats/'

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    # SELECT * from Cat
    return render(request, 'cats/index.html', { 'cats': cats})


def cats_details(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'