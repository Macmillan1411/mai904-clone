from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length=250)


class Book(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey("Department",on_delete=models.CASCADE,related_name='books')
    location = models.FilePathField((""))

class Task(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey("Department", on_delete=models.CASCADE,related_name='tasks')
    location = models.FilePathField((""))
    
    
class Onlinecourse(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name='onlinecourses')
    location = models.FilePathField((""))

class ThreeDModel(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name='online_courses')
    location = models.FilePathField((""))

