from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Main index page.
    url('^$', 'pages.views.index', name='pages_index'),
    url('about^$', 'pages.views.about', name='pages_about'),
    url('^terms$', 'pages.views.terms', name='pages_terms'),
    
)