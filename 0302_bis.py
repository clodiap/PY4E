heures = input("Combien d'heures travaillées ? ")
taux = input ("À quel taux horaire ? ")

#Calul de la paie en fonction du nb d'heures travaillées
def calcul_paie (hs, tx):
    if hs > 40.0 :
        txsup = tx * 1.5
        paiesup = hs * txsup
        print("Le montant de la paie est de", paiesup, "€")
    #sinon on garde le même taux
    else :
        paie = hs * tx
        print("Le montant de la paie est de", paie, "€")



# test si l'utilisateur a rentré un nombre
try :
    fheures = float(heures)
except :
    fheures = -1
    print("fheures = ",fheures)

try :
    ftaux = float(taux)
except :
    ftaux = -1
    print("ftaux = ",ftaux)

#s'il a rentré du texte, il aura un message d'erreur
if fheures == -1 :
    print("Il y a eu une erreur. Saisissez un nombre.")
    ffheures = float(input("Combien d'heures travaillées ? "))
    calcul_paie(ffheures,ftaux)

elif ftaux == -1 :
    print("Il y a eu une erreur. Saisissez un nombre.")
    fftaux = float(input("À quel taux horaire ? "))
    calcul_paie(fheures,fftaux)

else :
    calcul_paie(fheures, ftaux)
