from django.db import models

class School(models.Model):
    name = models.CharField(max_legnth = 100)
    location = models.CharField(max_length=100)

class Event(models.Model):
    name =
