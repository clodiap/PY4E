heures = input("Combien d'heures travaillées ? ")
taux = input ("À quel taux horaire ? ")

# test si l'utilisateur a rentré un nombre
try :
    fheures = float(heures)
except :
    fheures = -1

try :
    ftaux = float(taux)
except :
    ftaux = -1

#s'il a rentré du texte, il aura un message d'erreur
if fheures == -1 or ftaux == -1 :
    print("Il y a eu une erreur. Saisissez un nombre.")

else :
    # si heures travaillées > 40, le taux horaire est multiplié par 1.5
    if fheures > 40 :
        ftauxsup = ftaux * 1.5
        paiesup = fheures * ftauxsup
        print("Le montant de la paie est de", paiesup)
    #sinon on garde le même taux
    else :
        paie = fheures * ftaux
        print("Le montant de la paie est de", paie)
