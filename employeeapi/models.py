from django.db import models


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    employee_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15, blank=True)
