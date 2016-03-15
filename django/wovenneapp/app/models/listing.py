from django.conf import settings
from django.db import models

import simplejson as json


class Listing(models.Model):

    poster = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listings')
    title = models.CharField(max_length=256)
    description= models.CharField(max_length=1024)
    photo = models.ImageField(upload_to=b'static/app/img/listings/', help_text='Min size (90 x 58)px', null=True, blank=True)
    type = models.ForeignKey('ListingType', related_name='listings')
    category = models.ForeignKey('ListingCategory', related_name='listings')

    def to_dict(self):
        return {
            'poster': self.poster,
            'title': self.title,
            'description': self.description,
            'type': self.listing_type
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class ListingType(models.Model):

    name = models.CharField(max_length=256)

    def to_dict(self):
        return {
            'name': self.name
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class ListingCategory(models.Model):

    name = models.CharField(max_length=256)

    def to_dict(self):
        return {
            'name': self.name
        }

    def to_json(self):
        return json.dumps(self.to_dict())