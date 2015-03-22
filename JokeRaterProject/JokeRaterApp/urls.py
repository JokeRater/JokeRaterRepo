from django.conf.urls import patterns, url
from JokeRaterApp import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^register_profile/', views.register_profile, name='register_profile'),
	url(r'^profile/', views.profile, name='profile'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^joke/(?P<category_name_slug>[\w\-]+)/$', views.joke, name='joke'),
        url(r'^topOverall/', views.overall, name='topOverall'),
        url(r'^topWeekly/', views.weekly, name='topWeekly'),
        url(r'^search/', views.search, name='search'),
        )
		
