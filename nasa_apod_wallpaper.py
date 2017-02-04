#!/usr/bin/python

import os
import requests
import time
from random import randint
from bs4 import BeautifulSoup as BS

user = 'navjot'

url = 'https://apod.nasa.gov/apod/'
r = requests.get(url)
soup = BS(r.text, "html.parser")
flag = 0

while flag is 0:
	try:
		image = soup.find_all('img')[0]['src']
		flag = 1
	except:					#Getting an image from archives if currently a non-image content is posted
		url2 = 'https://apod.nasa.gov/apod/archivepix.html'
		r = requests.get(url2)
		soup = BS(r.text, "html.parser")
		soup = soup.find_all('a')
		x = randint(0, len(soup))
		url2 = url + soup[x]['href']
		r = requests.get(url2)
		soup = BS(r.text, "html.parser")

url = url + image

os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri "myloxyloto"')
os.system('wget -O /home/'+user+'/Pictures/desktop_background.jpg ' + url)

time.sleep(5)				#15 seconds time to allow proper download of picture
flag = 5
if flag is 5:
	os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:///home/'+user+'/Pictures/desktop_background.jpg')
	os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options "stretched"')
