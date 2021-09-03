import urllib
import urllib.request
import re

firstState = input('your state pls: ')
html = urllib.request.urlopen(f"https://www.homelessshelterdirectory.org/state/{firstState}")
cities = re.findall(r"(?P<url>https?://[^\s]+)", html.read().decode())
cities = [i for i in cities if '/city/' in i]
print(f'Cities in {firstState}:')
for i in cities:
  print(i)

html = urllib.request.urlopen("https://www.homelessshelterdirectory.org/city/ca-big_bear_city")
videoIDs = re.findall(r"(?P<url>https?://[^\s]+)", html.read().decode())
videoIDs = [i for i in videoIDs if '/shelter/' in i]
videoIDs = videoIDs[:10]
newList = []

for i in videoIDs:
  if '"><img' in i:
    i = i.replace('"><img', "")
    newList.append(i)

print('Homeless Shelters in Anaheim, CA:')
for i in newList: print(i)