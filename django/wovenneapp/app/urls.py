from django.conf.urls import patterns, url

urlpatterns = patterns('',

    url('^$', 'pages.views.index', name='app_index'),
    url('^profile$', 'pages.views.profile', name='app_profile'),

    # Listing crud operations
    url('^listing/new', 'pages.views.new_listing', name='app_new_listing'),
    url('^listing', 'pages.views.listings', name='app_listings'),
    url('^listing/(?P<listing_id>[0-9]+)', 'pages.views.listing', name='app_listing'),
    url('^listing/delete/(?P<listing_id>[0-9]+)', 'pages.views.delete_listing', name='app_delete_listing'),

)