from django.db import models

# Create your models here.
class Teacher(models.Model):
    fname = models.CharField(max_length = 20)
    iname = models.CharField(max_length = 20)
    sname = models.CharField(max_length = 20)
    status = models.CharField(max_length = 40)
    image = models.CharField(max_length = 200)
    

    def __str__(self) -> str:
        return self.fname + self.sname


