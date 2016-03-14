from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',

    url('^$', 'app.views.feed', name='app_feed'),


)