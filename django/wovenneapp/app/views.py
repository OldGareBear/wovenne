from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from app.models import Listing


def login(request):
    return render_to_response("app/html/login.html",
                              {},
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