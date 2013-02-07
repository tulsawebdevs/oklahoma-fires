from django.db import models

class Location(models.Model):
    latitude = models.DecimalField(max_digits=13, decimal_places=7)
    longitude = models.DecimalField(max_digits=13, decimal_places=7)
    brightness = models.DecimalField(max_digits=5, decimal_places=1)
    scan = models.DecimalField(max_digits=5, decimal_places=1)
    track = models.DecimalField(max_digits=5, decimal_places=1)
    acq_datetime = models.DateTimeField()
    satellite = models.CharField(max_length=1)
    confidence = models.IntegerField()
    version = models.DecimalField(max_digits=5, decimal_places=1)
    bright_t31 = models.DecimalField(max_digits=5, decimal_places=1)
    frp = models.DecimalField(max_digits=5, decimal_places=1)
