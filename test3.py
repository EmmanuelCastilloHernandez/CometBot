import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
import os

#extract playlist id from url
url = 'https://www.youtube.com/playlist?list=PLaV4k-99lpBWDfcR5vZkYlRUFHVXKQu2j'
query = parse_qs(urlparse(url).query, keep_blank_values=True)
playlistID = query["list"][0]

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = os.getenv('ytKey'))

request = youtube.playlistItems().list(
  part = "snippet",
  playlistId = playlistID,
  maxResults = 50
)
response = request.execute()

playlistItems = []
while request is not None:
  response = request.execute()
  playlistItems += response["items"]
  request = youtube.playlistItems().list_next(request, response)

result = [f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}' for t in playlistItems]

print(f"total: {len(playlistItems)}")
print(result)