from django.db import models
import random
from datetime import timedelta

def hex_color():
    return "#{0}".format(("%x" % random.randint(1, 16777215)).ljust(6, '0'))


class Especies(models.Model):
    """
    Each litlle rectangle inside the Farm
    """
    name = models.CharField(max_length=60)
    color = models.CharField(max_length=60,default=hex_color)
    interval_regar = models.DurationField(default=timedelta(days=2))


    def __str__(self):
        return self.name
