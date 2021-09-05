import urllib
import urllib.request
import re

firstState = input('your state pls: ').lower()
while ' ' in firstState:
  firstState = firstState.replace(' ', '_')
html = urllib.request.urlopen(f"https://www.homelessshelterdirectory.org/state/{firstState}")
cities = re.findall(r"(?P<url>https?://[^\s]+)", html.read().decode())
cities = re.findall(r"(?P<url>https?://[^\s]+)", str(cities))
cities = [i for i in cities if '/city/' in i]
stateAbv = cities[0][45:49]
cities = [i for i in cities if stateAbv in i]
stateCities = []

for i in cities:
  i = str(i)
  i = i.split('">')
  stateCities.append(i[0])

cityToChoose = input('enter your city (not county): ')
while ' ' in cityToChoose:
  cityToChoose = cityToChoose.replace(' ', '_')

for i in stateCities:
  if cityToChoose in i:
    city = i

html = urllib.request.urlopen(city)
videoIDs = re.findall(r"(?P<url>https?://[^\s]+)", html.read().decode())
videoIDs = [i for i in videoIDs if ('/shelter/' in i and 'listing.slug' not in i)]
videoIDs = videoIDs[:10]
newList = []

for i in videoIDs:
  if '"><img' in i:
    i = i.replace('"><img', "")
    newList.append(i)

print('Homeless Shelters in {}, {}:'.format(cityToChoose, firstState.upper()))
for i in newList: print(i)