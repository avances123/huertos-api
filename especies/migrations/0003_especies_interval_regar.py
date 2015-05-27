# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('especies', '0002_especies_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='especies',
            name='interval_regar',
            field=models.DurationField(default=datetime.timedelta(2)),
        ),
    ]
