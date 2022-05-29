from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True, default='')
    session = models.CharField(max_length=20)
    location = models.CharField(max_length=100)