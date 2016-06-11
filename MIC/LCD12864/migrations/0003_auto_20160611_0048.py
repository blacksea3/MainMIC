# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LCD12864', '0002_word_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailWord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('edittime', models.DateTimeField()),
                ('keyword', models.CharField(max_length=20)),
                ('index', models.CharField(max_length=4)),
                ('content', models.CharField(max_length=3)),
                ('state', models.SmallIntegerField()),
                ('ttype', models.IntegerField()),
            ],
            options={
                'db_table': 'MIC_LCDDetail',
            },
        ),
        migrations.CreateModel(
            name='LineWord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('vowel', models.CharField(max_length=20)),
                ('edittime', models.DateTimeField()),
                ('state', models.SmallIntegerField()),
                ('content', models.CharField(max_length=100)),
                ('index', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('ttype', models.IntegerField()),
            ],
            options={
                'db_table': 'MIC_LCD12864word',
            },
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
