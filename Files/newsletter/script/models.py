from django.db import models

# Create your models here.

class Newsletters(models.Model):
    newsletters = models.FileField(upload_to = 'newsletters/')
    
