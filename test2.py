from urllib.parse import parse_qs, urlparse
import urllib
import urllib.request
import re

html = urllib.request.urlopen("https://www.homelessshelterdirectory.org/city/ca-anaheim")
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