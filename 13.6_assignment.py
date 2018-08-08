import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# urlinput = input("Enter location:")
data = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_42.xml")

tree = ET.parse(data)
root = tree.getroot()

lst = root.findall("comments/comment")
print(lst)

listofcount = list()
for item in lst:

  print("count", item.find('count').text)




