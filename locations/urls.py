from django.conf.urls import patterns, url

from locations.views import LocationView

urlpatterns = patterns(
    '',
    url(r'^$', LocationView.as_view(), name='location_list'),
)
