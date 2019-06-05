from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DogToy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=255)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dog_toys = models.ManyToManyField(DogToy)

    def __str__(self):
        return self.name
