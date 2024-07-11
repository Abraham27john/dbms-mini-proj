from django.db import models
class Driver(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class Race(models.Model):
    race_name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)

class Result(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    position = models.IntegerField()
    points = models.IntegerField()