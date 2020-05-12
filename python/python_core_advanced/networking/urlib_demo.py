#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.error import HTTPError

from sys import exit

uri = "https://www.python.org"
page = None

try:

    page = urlopen(uri)
    content = page.read()

except HTTPError:
    print(f"URI: {uri} not found")
    exit()
except ValueError:
    print("Invalid uri")
    exit()
finally:
    if bool(page):
        page.close()

if bool(content):
    try:
        f = open("page_content.html", "wb")
        f.write(content)
    finally:
        f.close()

