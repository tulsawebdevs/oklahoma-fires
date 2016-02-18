# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=13)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=13)),
                ('brightness', models.DecimalField(decimal_places=1, max_digits=5)),
                ('scan', models.DecimalField(decimal_places=1, max_digits=5)),
                ('track', models.DecimalField(decimal_places=1, max_digits=5)),
                ('acq_datetime', models.DateTimeField()),
                ('satellite', models.CharField(max_length=1)),
                ('confidence', models.IntegerField()),
                ('version', models.DecimalField(decimal_places=1, max_digits=5)),
                ('bright_t31', models.DecimalField(decimal_places=1, max_digits=5)),
                ('frp', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]
