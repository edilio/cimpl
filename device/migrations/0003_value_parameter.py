# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_device_last_connection'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='parameter',
            field=models.ForeignKey(to='device.Parameter', default=1, to_field='id'),
            preserve_default=False,
        ),
    ]
