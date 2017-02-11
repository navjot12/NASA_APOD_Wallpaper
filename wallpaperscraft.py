#!/usr/bin/python

#Script to set wallpaper from https://wallpaperscraft.com/

import os
import requests
import time
from random import randint
from bs4 import BeautifulSoup as BS

user = 'navjot'
categories = ['abstract', 'city', 'cars', 'nature', 'space']			#Change this if wallpapers from other categories needed
x = randint(0, len(categories)-1)

url = 'https://wallpaperscraft.com/catalog/' + categories[x]
r = requests.get(url)
soup = BS(r.text, "html.parser")

number_of_pages = soup.find_all('div', {'class' : 'pages'})[0].find_all('a', {'class' : 'page_select'})[-1].text
x = randint(1, int(number_of_pages))
if x > 1:
	url = url + '/page' + str(x)

r = requests.get(url)
soup = BS(r.text, "html.parser")

images = soup.find_all('div', {'class': 'wallpaper_pre'})
x = randint(0, 14)
image = images[x].find('div', {'class' : 'pre_size'}).find('a')['href']
res = image[-9:]
image = image.split('//')[1].replace('/download/', '/image/').split('/'+res)[0]
image = image + '_' + res + '.jpg'

os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri "myloxyloto"')
os.system('wget -O /home/' + user + '/Pictures/desktop_background.jpg ' + image)

time.sleep(5)				#5 seconds time to allow proper download of picture
x = -1
if x is -1:
	os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:///home/' + user + '/Pictures/desktop_background.jpg')
	os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options "stretched"')