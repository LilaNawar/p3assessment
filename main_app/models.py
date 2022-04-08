from asyncio.windows_events import NULL
from django.db import models
from asyncio.windows_events import NULL
from secrets import choice
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class WackyWidgets(models.Model):
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def get_absolute_irl(self):
        return reverse('', kwargs={'pk': self.id})
