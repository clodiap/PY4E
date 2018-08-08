import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

urlinput = input("Enter rss feed (xml format): ")
if urlinput =="" :
  urlinput = "https://slashdot.org/slashdot.xml"
data = urllib.request.urlopen(urlinput)
print("Retrieving ", urlinput)

# on transforme le fichier xml en tree
tree = ET.parse(data)
root = tree.getroot()

titles = root.findall('.//title')

# Création d'une boucle qui récupère les titres
for item in titles:
  titre = item.text
  print("***" , titre)

