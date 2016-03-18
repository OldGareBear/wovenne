from django.conf.urls import patterns, url

urlpatterns = patterns('',

    url('^$', 'app.views.index', name='app_index'),
    url('^profile/$', 'app.views.profile', name='app_profile'),

    url('^login/$', 'app.views.login', name='app_login'),

    # Listing crud operations
    url('^listing/new', 'app.views.new_listing', name='app_new_listing'),
    url('^listing', 'app.views.listings', name='app_listings'),
    url('^listing/(?P<listing_id>[0-9]+)', 'app.views.listing', name='app_listing'),
    url('^listing/delete/(?P<listing_id>[0-9]+)', 'app.views.delete_listing', name='app_delete_listing'),

)