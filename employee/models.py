from django.db import models

class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.name
