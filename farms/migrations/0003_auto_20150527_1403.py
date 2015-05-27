# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0002_auto_20150527_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, srid=4326, null=True),
        ),
    ]
