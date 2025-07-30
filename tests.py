from django.test import TestCase

# Create your tests here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django World!")
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name
