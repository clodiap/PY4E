import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# urlinput = input("Enter location:")
urlinput = "http://py4e-data.dr-chuck.net/comments_42.xml"
data = urllib.request.urlopen(urlinput)
print("Retrieving ", urlinput)

# comptage des caractères
comptage = urllib.request.urlopen(urlinput).read()
print('Retrieved', len(comptage), 'characters')

# on transforme le fichier xml en tree
tree = ET.parse(data)
root = tree.getroot()

# on récupère l'intérieur des tags comments/comment
lst = root.findall("comments/comment")
# print(lst)

# Création d'une liste puis d'une boucle qui récupère les valeurs des tags count
listofcount = list()
for item in lst:
  nombre = item.find('count').text
  # print(nombre)
  inombre = int(nombre)
  listofcount.append(inombre)

# affichage de la somme des valeurs stockées dans la liste listofcount
print("Count:", len(listofcount))
print("Sum:", sum(listofcount))
