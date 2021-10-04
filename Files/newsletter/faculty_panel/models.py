from django.db import models
import os

# Create your models here.
class Highlights(models.Model):
    faculty_name = models.CharField(max_length=100)
    achievement = models.TextField()
    image = models.ImageField(upload_to='images')

class Milestones(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images')

class Activities(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    caption = models.CharField(max_length=200)

class Placements(models.Model):
    company = models.CharField(max_length=200)
    number = models.IntegerField()

class Students(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images')

class Events(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images')

class Projects(models.Model):
    description = models.TextField()

class Phd(models.Model):
    description = models.TextField()

