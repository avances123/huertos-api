# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('especies', '0003_especies_interval_regar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=60)),
                ('width', models.FloatField(default=4.0)),
                ('height', models.FloatField(default=2.0)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('sizex', models.PositiveSmallIntegerField(default=2)),
                ('sizey', models.PositiveSmallIntegerField(default=2)),
                ('col', models.PositiveSmallIntegerField(default=0)),
                ('row', models.PositiveSmallIntegerField(default=0)),
                ('especies', models.ForeignKey(to='especies.Especies',on_delete=models.CASCADE, null=True)),
                ('farm', models.ForeignKey(to='farms.Farm',on_delete=models.CASCADE,)),
            ],
        ),
    ]
