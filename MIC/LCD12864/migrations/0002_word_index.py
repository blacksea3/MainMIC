# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LCD12864', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='index',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
