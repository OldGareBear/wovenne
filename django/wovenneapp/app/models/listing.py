from django.conf import settings
from django.db import models

import simplejson as json


# class Listing(models.Model):
#
#     poster = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listings')
#     title = models.CharField(max_length=256)
#     description= models.CharField(max_length=1024)
#     photo = models.ImageField(upload_to=b'static/app/img/listings/', help_text='Min size (90 x 58)px', null=True, blank=True)
#     listing_type = models.ForeignKey('ListingType', related_name='type')
#
#     def to_json(self):
#         return json.dumps({
#             'poster': self.poster,
#             'title': self.title,
#             'description': self.description,
#             'type': self.listing_type
#         })


class ListingType(models.Model):

    name = models.CharField(max_length=256)

    def to_json(self):
        return json.dumps({
            'name': self.name
        })