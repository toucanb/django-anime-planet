from django.conf.urls import patterns, url
from anime_planet import views

urlpatterns = patterns('',
	# ex: http://www.exemple.com/animelist/
	url(r'^$', views.displayAnime, name='animelist'),
	# You want to make the refresh URL secret to avoid disc operations.
	# HTTP or Django authentication could also be used.
	# ex: http://www.exemple.com/animelist/refresh/
	url(r'^refresh/$', views.refreshAnime, name='refreshAnime'),
)
