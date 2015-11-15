# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password_reset_code', models.CharField(default=b'', max_length=100)),
                ('age', models.CharField(default=b'', max_length=8)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=b'', max_length=256)),
                ('title', models.CharField(default=b'', max_length=64)),
                ('artist', models.ForeignKey(to='account.Artist', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='profile',
            field=models.ForeignKey(to='account.Profile', null=True),
        ),
    ]
