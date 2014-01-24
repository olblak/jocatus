from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'jocatus.game.views.index',name='news'),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^accounts/', include('allauth.urls')),
	url(r'^library_game/(?P<game>\w+)','jocatus.game.views.game',name='game'), # Un ordre a respecter?
	url(r'^library_game/', 'jocatus.game.views.library_game', name='library_game'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print settings.MEDIA_ROOT
print settings.MEDIA_URL
