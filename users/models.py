from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Farmer(models.Model):
    user = models.OneToOneField(User)
    # extend model here


    def __str__(self):
        return u'%s' % (self.user.username)



def create_farmer(sender,created,instance, **kw):
    if created:
        farmer = Farmer(user=instance)
        farmer.save()

post_save.connect(create_farmer, sender=User)