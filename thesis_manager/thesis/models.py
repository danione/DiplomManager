from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    number = models.SmallIntegerField(default=1)
    curent_class = models.CharField(max_length=10)
    systems_networks = models.CharField(max_length=2)
    overall_grade = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    titles = models.CharField(max_length=100)
    systems_networks = models.CharField(max_length=2)

class Thesis_Topic(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    systems_networks = models.CharField(max_length=2)
