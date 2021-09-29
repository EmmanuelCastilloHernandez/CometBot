import urllib
import urllib.request
import requests
from requests import get
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen("https://open.spotify.com/playlist/0zbuDTZROsRwyrpVHcD6wh?si=93585d3d753d4820")
playlist = re.findall(r"(?P<url>https?://[^\s]+)", html.read().decode())
playlist = re.findall(r"(?P<url>https?://[^\s]+)", str(playlist))
playlist = [i for i in playlist if 'https://open.spotify.com/track/' in i]

songs = []
for i in playlist:
  i = str(i)
  i = i.split('"')
  if i[0] not in songs and '/artist/' not in i[0]:
    songs.append(i[0])