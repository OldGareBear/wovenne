import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from app.models import Listing, UserProfile
from facebook import FacebookAPI

User = settings.AUTH_USER_MODEL


def login(request):
    if request.method == 'POST':
        access_token = _get_access_token(request)
        user = _get_or_create_user(request, access_token)


    return render_to_response("app/html/login.html",
                              {'host': settings.HOSTNAME},
                              context_instance=RequestContext(request))


@login_required
def index(request):
    return render_to_response("app/html/index.html",
                              {},
                              context_instance=RequestContext(request))


@login_required
def profile(request):
    return render_to_response("app/html/profile.html",
                              {},
                              context_instance=RequestContext(request))


@login_required
def new_listing(request):
    return render_to_response("app/html/new_listing.html",
                              {},
                              context_instance=RequestContext(request))


@login_required
def listings(request):
    if not request.method == 'POST':
        raise Exception("Invalid Protocol")

    # create new listing
    pass


@login_required
def listing(request, listing_id):
    listing = Listing.objects.filter(id=listing_id).first()

    if request.method in ['PATCH', 'PUT']:
        # update listing
        pass

    return render_to_response("app/html/listing.html",
                              {},
                              context_instance=RequestContext(request))


@login_required
def delete_listing(request):
    return render_to_response("app/html/terms.html",
                              {},
                              context_instance=RequestContext(request))

def _get_access_token(request):
    short_lived_token = request.POST.get('authResponse[accessToken]')
    fb = FacebookAPI(settings.FB_CLIENT_ID, settings.FB_SECRET)
    return fb.get_long_lived_token(short_lived_token)

def _get_or_create_user(request, access_token):
    post_data = request.POST
    logging.info(post_data)
    # user_profile = UserProfile.objects.get(facebook_id=)

