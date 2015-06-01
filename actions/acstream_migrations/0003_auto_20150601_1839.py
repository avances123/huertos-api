# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0002_auto_20150527_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='action_object_object_id',
            field=models.CharField(max_length=255, blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='actor_object_id',
            field=models.CharField(max_length=255, db_index=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='public',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='target_object_id',
            field=models.CharField(max_length=255, blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='action',
            name='verb',
            field=models.CharField(max_length=255, db_index=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='object_id',
            field=models.CharField(max_length=255, db_index=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='started',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
