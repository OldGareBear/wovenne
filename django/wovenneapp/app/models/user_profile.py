from django.conf import settings
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    facebook_id = models.CharField(max_length=300)
    facebook_token = models.CharField(max_length=300, null=True, blank=True)
