from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)