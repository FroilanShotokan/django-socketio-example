from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'/echo$', 'playground.views.echo'),
    url(r'/time$', 'playground.views.time'),
    url(r'/chat$', 'playground.views.chat'),
)
