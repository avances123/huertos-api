# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import especies.models


class Migration(migrations.Migration):

    dependencies = [
        ('especies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='especies',
            name='color',
            field=models.CharField(max_length=60, default=especies.models.hex_color),
        ),
    ]
