from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellocities.views.home', name='home'),
    url(r'^locations/', include('locations.urls')),
    url(r'^$', RedirectView.as_view(url="locations/")),
    url(r'^admin/', include(admin.site.urls)),
)
