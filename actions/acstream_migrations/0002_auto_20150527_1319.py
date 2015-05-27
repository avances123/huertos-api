# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='data',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
