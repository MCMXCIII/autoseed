# -*- coding:utf-8 -*-
import requests
import sys
import json

r_url = "https://nyaa.pantsu.cat/api/search"
data = requests.get(r_url).json()
if not data:
     print('No data found.')
i=1
#make varibale for the the index to compare values
index = 0
torrent = 0
seeder = 0 
leecher = 0
for values in data['torrents']:
     if values['seeders'] < leecher and values['leechers'] > seeder:
          seeder = values['seeders']
          leecher = values['leechers']
          torrent = index
     index +=1
    # print(torrent)
     print(data['torrents'][torrent])


#Listing function done!^^^^^^^^^^^^^





