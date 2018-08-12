import json
import urllib.request, urllib.parse, urllib.error

# url de test
urldetest = "http://py4e-data.dr-chuck.net/comments_42.json"

urlinput = input("Enter location: ")
if len(urlinput) < 1:
    urlinput = urldetest
data = urllib.request.urlopen(urlinput)
print("Retrieving ", urlinput)

# comptage des caractères
content = urllib.request.urlopen(urlinput).read()
print('Retrieved', len(content), 'characters')

# extraction du format json (en liste et dictionnaire)
datajson = json.loads(content)

# affiche le json avec les indentations
# print(json.dumps(datajson, indent=4))

# récupération du dictionnaire 'comments' et création d'une liste avec les valeurs 'count' du dictionnaire
comments = datajson['comments'] # value 'comments'
listitems = list()
for item in comments:
    listitems.append(item['count'])

# somme des nombres de 'count' (maintenant dans listitems)
sumnumber = 0
for number in listitems:
    inumber = int(number)
    sumnumber += inumber

print("Count:", len(listitems))
print("Sum:", sumnumber)
