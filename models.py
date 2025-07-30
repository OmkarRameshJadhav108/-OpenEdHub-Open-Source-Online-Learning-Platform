from django.db import models

class Product(models.Model):  # ✅ Capital 'Model'
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.name
