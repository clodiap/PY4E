import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# avec utilisation de XPath

# url de test
urlinput = "http://py4e-data.dr-chuck.net/comments_42.xml"

# urlinput = input("Enter location: ")
data = urllib.request.urlopen(urlinput)
print("Retrieving ", urlinput)

# comptage des caractères
comptage = urllib.request.urlopen(urlinput).read()
print('Retrieved', len(comptage), 'characters')

# on transforme le fichier xml en tree
tree = ET.parse(data)
root = tree.getroot()

counts = root.findall('.//count')

# Création d'une liste puis d'une boucle qui récupère les valeurs des tags count
listofcount = list()
for item in counts:
  nombre = item.text
  # print(nombre)
  inombre = int(nombre)
  listofcount.append(inombre)

# affichage de la somme des valeurs stockées dans la liste listofcount
print("Count:", len(listofcount))
print("Sum:", sum(listofcount))
