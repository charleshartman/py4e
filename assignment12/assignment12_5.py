#py4e assignment 12.5

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)
print('Retrieving:', url)
while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #get the href at value of [position]
    tag = tags[position - 1]
    url = tag.get('href', None)
    print('Retrieving:', url)
    count = count - 1
