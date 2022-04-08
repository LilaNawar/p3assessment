from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import WackyWidgets
# Create your views here.


def home(request):
    widget_list = WackyWidgets.objects.all()
    return render(request, 'index.html', {'widget_list': widget_list})


def widget_add(request):
    WackyWidgets.objects.create(
        description=request.POST['description'], quantity=request.POST['quantity'])
    return redirect("/")


class WackyWidgetsDelete(DeleteView):
    model = WackyWidgets
    success_url = '/'
