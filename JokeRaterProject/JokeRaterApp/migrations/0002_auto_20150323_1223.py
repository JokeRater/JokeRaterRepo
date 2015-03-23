# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('JokeRaterApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='datePosted',
            field=models.DateField(default=datetime.date(2015, 3, 23)),
        ),
    ]
