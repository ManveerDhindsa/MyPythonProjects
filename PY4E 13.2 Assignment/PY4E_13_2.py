import json
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Url: ')
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

info = json.loads(data)

stuff = info['comments']

count = 0
total = 0
for comment in stuff:
    total += int(comment['count'])
    count += 1
print('count:', count)
print('Total:', total)