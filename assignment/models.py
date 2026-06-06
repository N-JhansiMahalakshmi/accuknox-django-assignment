from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)

class Log(models.Model):
    message=models.CharField(max_length=100)
