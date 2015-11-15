# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20151115_0325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='profile',
        ),
    ]
