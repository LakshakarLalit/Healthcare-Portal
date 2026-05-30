from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100000)
    age = models.IntegerField()
    disease = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)