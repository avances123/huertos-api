from django.contrib.gis.db import models
from django.contrib.auth.models import User
from especies.models import Especies
from django.db.models.signals import post_save
from actstream import action


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



def on_save(sender, instance, created, **kwargs):
    if created:
        action.send(instance.owner, verb='created',action_object=instance,color="#348923")
    else:
        action.send(instance.owner, verb='modified',action_object=instance,color="#348923")


post_save.connect(on_save, sender=Farm)
