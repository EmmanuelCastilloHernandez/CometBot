import urllib
import requests
from requests import get
import urllib.request
import re
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://giphy.com/gifs/mlb-sports-baseball-asg-yD5KEKVG1o9qcoXNYg")
gifs = re.findall(r"(?P<url>https?://[^\s]+)", html.read().decode())
gifs = re.findall(r"(?P<url>https?://[^\s]+)", str(gifs))
gifs = [i for i in gifs if 'https://media0.giphy.com/' in i]
gifs2 = []

for i in gifs:
  i = str(i)
  i = i.split('">')
  i = gifs2.append(i[0])

print(gifs2)
