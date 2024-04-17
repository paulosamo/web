from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    location = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    location = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.name
