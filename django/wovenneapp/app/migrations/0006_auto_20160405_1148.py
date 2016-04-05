# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userprofile2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='facebook_id',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
    ]
