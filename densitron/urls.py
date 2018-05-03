from django.conf import settings
from django.conf.urls import url, include, patterns

from densitron.admin import admin_site


urlpatterns = [
    url(r'^admin/', admin_site.urls),

    url(r'', include('elastic_pages.special_urls')),
    url(r'', include('elastic_pages.urls'))
]

if settings.DEBUG and settings.TESTING:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}))

handler404 = 'elastic_pages.views.handler404'