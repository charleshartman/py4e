#py4e assignment 12.4

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_42.html"

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

y = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    #print('Contents:', tag.contents[0])
    if len(tag) > 0:
        for x in tag:
            tag = int(x)
            y = y + tag

print(y)
