from django.db import models

class studentModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    emailAddress = models.EmailField(unique=True)
    joining_Date = models.DateField(null=True)




class teacherModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    emailAddress = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_Date = models.DateField(null=True)

    
