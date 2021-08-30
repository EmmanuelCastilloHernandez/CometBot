from bs4 import BeautifulSoup
import requests
from requests import get

url = 'https://open.spotify.com/track/4HXOBjwv2RnLpGG4xWOO6N?si=15d4a200116b4639'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
print(soup.title)