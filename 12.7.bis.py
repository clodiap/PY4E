from urllib.request import urlopen
from bs4 import BeautifulSoup
# import ssl

# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
numbers = soup('span')
numberlist = list()
for number in numbers:
    # print("contents", number.contents[0])
    inumber = int(number.contents[0])
    numberlist.append(inumber)
print("Sum: ", sum(numberlist))
