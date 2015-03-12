from django.conf.urls import patterns, url
from JokeRaterApp import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^register_profile/', views.register_profile, name='register_profile'),)
		
