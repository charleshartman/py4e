#py4e assignment 13.1

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
counting = 0
total = 0
url = input('Enter - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_42.xml"
#if len(address) < 1: break

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')
#print(counts)
for item in counts:
    x = item.text
    y = int(x)
    total = y + total
    counting = counting + 1

print('Count:', counting)
print('Sum:', total)
