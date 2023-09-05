from django.db import models

# Create your models here.
class user(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=200)
    