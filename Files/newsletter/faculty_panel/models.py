from django.db import models
import os

# Create your models here.
class Highlights(models.Model):
    faculty_name = models.CharField(max_length=100)
    achievement = models.TextField()
    image = models.ImageField(upload_to='images')