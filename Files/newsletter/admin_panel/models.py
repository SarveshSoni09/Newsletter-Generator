from django.db import models

# Create your models here.
class Header(models.Model):
    academic_year = models.CharField(max_length=50)
    volume = models.CharField(max_length=10)
    semester = models.CharField(max_length = 5)
    department_image = models.ImageField(upload_to='images/')
    editorial_desk = models.TextField()