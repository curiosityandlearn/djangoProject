# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_auto_20150611_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software_service',
            name='taobao_id',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
