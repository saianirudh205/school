from django.db import models
from classes.models import Class

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
