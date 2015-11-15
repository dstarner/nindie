# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='last_played',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password_reset_code',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.CharField(default='', max_length=256),
        ),
    ]
