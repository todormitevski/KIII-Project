from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Band(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year_established = models.IntegerField()
    num_events = models.IntegerField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    poster = models.ImageField(upload_to='assets/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    band_input = models.CharField(max_length=200)
    is_outdoor = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class EventBand(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event.name} {self.band.name}"
