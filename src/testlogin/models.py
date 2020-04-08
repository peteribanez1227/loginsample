from django.db import models

class Employee(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=3)
    employeenum = models.CharField(max_length=11)
    teamlead = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    shiftschedule = models.CharField(max_length=20)

