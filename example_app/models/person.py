# models/person.py
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    class Meta:
        abstract = True