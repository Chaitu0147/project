
from django.db import models

# Create your models here.

class register(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    username = models.CharField(max_length=100)
    password = models.IntegerField(max_length=100)
    confirm = models.IntegerField(max_length=100)
    
class Student(models.Model):
    name=models.CharField(max_length=250)
    roll_number=models.IntegerField()

    def _str_(self):
        return self.name



class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=False)



    