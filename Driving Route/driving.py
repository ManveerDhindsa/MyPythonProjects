import urllib.request
import json

# Your Bing Maps Key 
bingMapsKey = "PUT_KEY_HERE" 

# input information

start = input('Start: ')
end = input('End: ')

encodedDest = urllib.parse.quote(end, safe='')
encodedDest1 = urllib.parse.quote(end, safe='')

routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + encodedDest + "&wp.1=" + encodedDest1 + "&key=" + bingMapsKey

request = urllib.request.Request(routeUrl)
response = urllib.request.urlopen(request)

r = response.read().decode(encoding="utf-8")
result = json.loads(r)

itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]

direction = 0
for item in itineraryItems:
    direction += 1
    print(f'Direction {direction}:', item["instruction"]["text"])