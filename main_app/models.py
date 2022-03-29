from asyncio.windows_events import NULL
from secrets import choice
from django.db import models
from django.urls import reverse

# Create your models here.


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    image = models.CharField(default=None, blank=True, null=True, max_length=2000)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'cat_id': self.id})


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

 