# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0003_auto_20150611_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software_service',
            name='ding_dan_hao',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='software_service',
            name='ping_ju',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='software_service',
            name='xian_xia_ke_hu',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
