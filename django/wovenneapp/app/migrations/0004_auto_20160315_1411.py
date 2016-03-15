# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_listingcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='listing_type',
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(related_name='listings', default=1, to='app.ListingCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.ForeignKey(related_name='listings', default=1, to='app.ListingType'),
            preserve_default=False,
        ),
    ]
