# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_artist_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='songs_played',
            field=models.IntegerField(default=0),
        ),
    ]
