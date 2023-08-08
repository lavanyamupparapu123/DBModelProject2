from django.db import models

# Create your models here.
class Employee2(models.Model):
    eno=models.IntegerField();
    ename=models.CharField(max_length=30);
    esal=models.FloatField();
    eaddr=models.CharField(max_length=30);


class Job(models.Model):
    postingdate=models.IntegerField(),
    location=models.CharField(max_length=30),
    offeredsalary=models.FloatField(),
    qualification=models.CharField(max_length=30),



