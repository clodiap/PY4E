import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# urlinput = input("Enter location:")
data = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_42.xml")

tree = ET.parse(data)
print(tree)

counts = tree.findall('.//name')
print("counts ", counts)


root = tree.getroot()
print(root)

for child in root:
    print(child.tag, child.attrib)


