from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    admission_number = models.CharField(unique=True)
    enrolled_date = models.DateField(auto_now_add=True)
    stream = models.CharField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    staff_id = models.CharField(unique=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

