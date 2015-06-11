# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='A_second',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taobao_id', models.CharField(max_length=200)),
                ('ding_dan_hao', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='software_service',
            name='ding_dan_hao',
            field=models.IntegerField(default=b'10000'),
        ),
        migrations.AddField(
            model_name='software_service',
            name='ping_ju',
            field=models.CharField(default=b'ping_ju', max_length=200),
        ),
        migrations.AddField(
            model_name='software_service',
            name='xian_xia_ke_hu',
            field=models.CharField(default=b'ke_hu', max_length=200),
        ),
        migrations.AlterField(
            model_name='software_service',
            name='taobao_id',
            field=models.CharField(default=b'id', max_length=200),
        ),
    ]
