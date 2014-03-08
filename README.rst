Django Anime Planet
===================

Django Anime Planet is a simple script that scrapes an anime list from an anime-planet profile and outputs it to a nice stylable html table.

It's actually just a plain python script inside a Django view, no models are used so no database is needed.

Requirements
------------

* Django 1.4+
* Python 3
* BeautifulSoup4

Installation
------------

As easy as::

	cd /django/project/
	python manage.py startapp anime_planet
	cd anime_planet
	git clone https://github.com/toucanb/django-anime-planet.git

Install requirements if it's not already done::

	pip install -r requirements.txt

Add the application to the project ``settings.py``::

	INSTALLED_APPS = (
		#...
		'anime_planet',
	)

Configure the project ``urls.py``::

	urlpatterns = patterns('',
		#...
		url(r'^animelist/', include('anime_planet.urls')),
	)

Add your anime-planet user in ``views.py`` and you're all set!

Changelog
---------

* 2014-03-08
	- Initial release.

Licence
-------

This project is licensed under the terms of the BSD 3-Clause License.

A copy of the licence is included.
