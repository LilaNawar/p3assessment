from asyncio.windows_events import NULL
from django.db import models
from django.urls import reverse

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    image = models.CharField(default=None, blank=True, null=True, max_length=2000)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'cat_id': self.id})

 