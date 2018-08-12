import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
      # address = 'South Federal University' # url de test

    # décodage de l'adresse (espaces transformés…)
    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    # récupérer le document avec read et le décoder (utf8 vers unicode)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    # comptage des caractères
    print('Retrieved', len(data), 'characters')

    # vérification de l'intégrité du JSON
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # affichage du json avec indentations
    # print(json.dumps(js, indent=4))

    # affiche la bonne valeur du bon dictionnaire de la bonne liste après moult tatonnements :)
    print("Place id", js["results"][0]['place_id'])

