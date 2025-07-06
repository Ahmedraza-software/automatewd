from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no= models.IntegerField(default=0)
    name= models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    
    