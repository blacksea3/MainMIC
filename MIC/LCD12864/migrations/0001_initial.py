# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('vowel', models.CharField(max_length=20)),
                ('edittime', models.DateTimeField()),
                ('state', models.SmallIntegerField()),
                ('content', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('ttype', models.IntegerField()),
            ],
            options={
                'db_table': 'MIC_LCD12864',
            },
        ),
    ]
