# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoutbox', '0002_auto_20150530_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
