from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.views import password_reset

class MyRegistrationView(RegistrationView):
    def get_success_url(selfself,request, user):
        return '/JokeRater/register_profile'
		
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^JokeRater/', include('JokeRaterApp.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
	)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
