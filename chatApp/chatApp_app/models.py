from django.db import models
from datetime import datetime
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)


class Message(models.Model):
    text = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=30)
    room = models.CharField(max_length=50)
