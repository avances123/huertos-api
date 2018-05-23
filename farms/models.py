from django.contrib.gis.db import models
from django.contrib.auth.models import User
from especies.models import Especies
from django.db.models.signals import post_save

class Farm(models.Model):
    """
    The big rectangle
    """
    owner   = models.ForeignKey(User,on_delete=models.CASCADE)
    name    = models.CharField(max_length=60)

    mpoly = models.MultiPolygonField(null=True)


    def __str__(self):
        return "{0} ({1} zones)".format(self.name,self.zone_set.count())


class Zone(models.Model):
    """
    Each litlle rectangle inside the Farm
    """
    farm     = models.ForeignKey(Farm,on_delete=models.CASCADE)
    especies = models.ForeignKey(Especies,on_delete=models.CASCADE,null=True)
    # layout
    cols    = models.PositiveSmallIntegerField(default=2)
    rows    = models.PositiveSmallIntegerField(default=2)
    x       = models.PositiveSmallIntegerField(default=0)
    y       = models.PositiveSmallIntegerField(default=0)
