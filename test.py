import requests
from requests import get
from bs4 import BeautifulSoup
import re
page = requests.get('https://giphy.com/gifs/mlb-sports-baseball-asg-yD5KEKVG1o9qcoXNYg')
soup = BeautifulSoup(page.content, "html.parser")

pageContent = soup.find(id="content")
giphyUrls = pageContent.find_all("div", class_="gif-detail-page", id='react-target')
print(giphyUrls)

giphyUrls = re.findall("(?P<url>https?://[^\s]+)", str(pageContent))

print(giphyUrls)