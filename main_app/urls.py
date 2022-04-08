from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.widget_add, name='create'),
    path('delete/<int:pk>/', views.WackyWidgetsDelete.as_view(), name='delete')
]
