import logging
import requests
import urllib
import urlparse


class FacebookAPI(object):

    API_URI_BASE = "https://graph.facebook.com/v2.5/oauth/"

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_long_lived_token(self, short_lived_token):
        uri = self._endpoint('access_token',
                             grant_type='fb_exchange_token',
                             client_id=self.client_id,
                             client_secret=self.client_secret,
                             fb_exchange_token=short_lived_token)
        response = requests.get(uri)
        response_json = response.json()
        return response_json.get('access_token') if response.ok else None

    def _endpoint(self, service, **kwargs):
        uri = urlparse.urljoin(self.API_URI_BASE, service)
        if kwargs:
            uri += '?' + urllib.urlencode(kwargs)
        return uri
