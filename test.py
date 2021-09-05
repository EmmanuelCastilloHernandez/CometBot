import requests
from requests import get
from bs4 import BeautifulSoup
import re
page = requests.get('https://www.homelessshelterdirectory.org/city/ca-van_nuys')
soup = BeautifulSoup(page.content, "html.parser")
giphyUrls = re.findall("(?P<url>https?://[^\s]+)", str(soup))
videoIDs = [i for i in giphyUrls if ('/shelter/' in i and 'listing.slug' not in i)]
videoIDs = videoIDs[:10]
newList = []

for i in videoIDs:
  if '"><img' in i:
    i = i.replace('"><img', "")
    newList.append(i)


print(newList)