# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('photo', models.ImageField(help_text=b'Min size (90 x 58)px', null=True, upload_to=b'static/app/img/listings/', blank=True)),
                ('listing_type', models.ForeignKey(related_name='type', to='app.ListingType')),
                ('poster', models.ForeignKey(related_name='listings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('facebook_id', models.IntegerField(default=1, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
