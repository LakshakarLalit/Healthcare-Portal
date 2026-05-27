from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=5000)
    about = models.TextField()
    specilization = models.CharField(max_length=100)
    degree = models.CharField(max_length=500)
    experience = models.IntegerField()
    hospital_name = models.CharField(max_length=500)