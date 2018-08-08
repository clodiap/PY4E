# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# import ssl

# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

def openurl(url, count, position) :
    while count >= 0 :
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        listlinks = list()
        for tag in tags:
            listlinks.append(tag.get("href", None))
        print("Retrieving: ", url)
        url = listlinks[position-1]
        count -= 1


# enterurl = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# enterurl = "http://py4e-data.dr-chuck.net/known_by_Lina.html"
enterurl = input("Enter url: ")
entercount = input("Enter count: ")
enterposition = input("Enter position: ")

openurl(enterurl, int(entercount), int(enterposition))
