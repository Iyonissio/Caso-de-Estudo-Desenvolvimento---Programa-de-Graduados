import datetime
from pyexpat import model
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils import tree
from .api.models.models import ControlModel
from datetime import date


class Employeer(ControlModel):
    name = models.CharField(('Nome'), max_length=254)
    company = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    validate = models.DateField(
        ('Validade'), null=True, blank=True, default=datetime.date.today)

    def __str__(self):
        return self.name

class Transporte(models.Model):
    som_id = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude1 = models.CharField(max_length=100)
    longitude1 = models.CharField(max_length=100)

class RequestControlUssd(models.Model):
    phone = models.CharField(max_length=15)
    trasantion_type = models.CharField(max_length=150)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.phone

class RequestsUssd(models.Model):
    phone = models.CharField(max_length=15)
    trasantion_type = models.CharField(max_length=150)
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.phone
