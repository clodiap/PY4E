import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# url de test
urlinput = "https://slashdot.org/slashdot.xml"
# urlinput = "https://foudechats.fr/feed/"

# urlinput = input("Enter rss feed (xml format): ")
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

