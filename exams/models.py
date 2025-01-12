from django.db import models
from subjects.models import Subject

class Exam(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    subjects = models.ManyToManyField(Subject)
