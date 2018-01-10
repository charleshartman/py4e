#py4e assignment 13.2

import urllib.request, urllib.parse, urllib.error
import json

counting = 0
total = 0
url = input('Enter - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_42.json"
#if len(address) < 1: break

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
#print(json.dumps(js, indent=4))
counts = js["comments"]
#print(counts)
for item in counts:
    x = item["count"]
    y = int(x)
    total = y + total
    counting = counting + 1

print('Count:', counting)
print('Sum:', total)
