# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0003_auto_20150527_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farm',
            old_name='mpoly',
            new_name='poly',
        ),
    ]
