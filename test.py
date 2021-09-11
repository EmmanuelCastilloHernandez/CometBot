import urllib
import urllib.request
import requests
from requests import get
from bs4 import BeautifulSoup
import re

firstState = input('your state pls: ').lower()
while ' ' in firstState:
  firstState = firstState.replace(' ', '_')
html = urllib.request.urlopen(f"https://www.freetreatmentcenters.com/state/{firstState}")
cities = re.findall(r"(?P<url>https?://[^\s]+)", html.read().decode())
cities = re.findall(r"(?P<url>https?://[^\s]+)", str(cities))
cities = [i for i in cities if '/ci/' in i]
stateAbv = cities[0][39:43]
cities = [i for i in cities if stateAbv in i]
stateCities = []

for i in cities:
  i = str(i)
  i = i.split('"\',')
  stateCities.append(i[0])

cityToChoose = str(input('enter your city (not county): '))
while ' ' in cityToChoose:
  cityToChoose = cityToChoose.replace(' ', '_')
print(stateCities)

for i in stateCities:
  if cityToChoose in i:
    city = i
    print(city)
    if i[43:] == cityToChoose:
      break

page = requests.get(city)
soup = BeautifulSoup(page.content, "html.parser")
counter = soup.find_all("p")
counter = [i.get_text() for i in counter]
counter = counter[1].replace('                    ', '').split('\n')
counter = counter[1:len(counter)-1]
for count, i in enumerate(counter): counter[count] = i.replace('\r', '')
counter[0:2] = [', '.join(counter[0:2])]
print(counter)
