#! python3
# -*-coding:utf-8 -*

# Python 3 - http://python.org/download/
# Django 1.4 - https://www.djangoproject.com/
# BeautifulSoup 4 - http://www.crummy.com/software/BeautifulSoup/

# This script will scrape a list from http://www.anime-planet.com and export it to html.

from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup,NavigableString
import urllib.request,urllib.error,urllib.parse,sys,re,codecs

def refreshAnime(request):
	username = ';)' #PUT YOUR ANIME-PLANET USER HERE.
	userAgent = 'Mozilla/5.0'
	baseURL = 'http://www.anime-planet.com/users/'+username+'/anime'
	req = urllib.request.Request(baseURL)
	req.add_header("User-Agent",  userAgent)
	html = BeautifulSoup(urllib.request.urlopen(req).read())
	pageNumber = int (html.find('li','next').findPrevious('li').next.contents[0])
	f = codecs.open('anime_planet/templates/anime-planet.html', 'w', 'utf-8')
	for i in range(1,pageNumber+1):
		baseURL = 'http://www.anime-planet.com/users/'+username+'/anime?page='+str(i)
		req = urllib.request.Request(baseURL)
		req.add_header("User-Agent",  userAgent)
		html = BeautifulSoup(urllib.request.urlopen(req).read())
		for animeItem in html.findAll('tr')[1:]:
			animeItem = BeautifulSoup(animeItem.renderContents())
			f.write('\t<tr class="' + animeItem.find('td','tableStatus').text.replace('status box','').replace(' ','_') + '">\n')
			f.write('\t\t<td class="animetitle"><a href="http://anime-planet.com' + animeItem.a['href'] +'">' + animeItem.a.text + '</a></td>\n')
			f.write('\t\t<td class="type">' + animeItem.find('td','tableType').text + '</td>\n')
			f.write('\t\t<td class="year">' + animeItem.find('td','tableYear').text + '</td>\n')
			f.write('\t\t<td class="episodes">' + animeItem.find('td','tableEps').text.replace('&nbsp;','1') + '</td>\n')
			score = str(int(float(animeItem.img['name']))).replace('0','').replace('1','★').replace('2','★★').replace('3','★★★').replace('4','★★★★').replace('5','★★★★★')
			f.write('\t\t<td class="score">' + score + '</td>\n')
			f.write('\t</tr>\n\n')
	f.close()
	return HttpResponse('Anime list has been refreshed. Click <a href="../">here</a> to return to the list.')

def displayAnime(request):
	return render(request, 'animelist.html')
