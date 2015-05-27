# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('especies', '0002_especies_color'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('width', models.FloatField(default=4.0)),
                ('height', models.FloatField(default=2.0)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sizex', models.PositiveSmallIntegerField()),
                ('sizey', models.PositiveSmallIntegerField()),
                ('col', models.PositiveSmallIntegerField()),
                ('row', models.PositiveSmallIntegerField()),
                ('especies', models.ForeignKey(to='especies.Especies', null=True)),
                ('farm', models.ForeignKey(to='farms.Farm')),
            ],
        ),
    ]
