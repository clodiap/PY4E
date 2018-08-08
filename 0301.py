heures = input("Combien d'heures travaillées ? ")
taux = input ("À quel taux horaire ? ")

#transformation en float
fheures = float(heures)
ftaux = float(taux)

# si heures travaillées > 40, le taux horaire est multiplié par 1.5
if fheures > 40 :
    ftauxsup = ftaux * 1.5
    paiesup = fheures * ftaux
    print("Le montant de la paie est de", paiesup)
#sinon on garde le même taux
else :
    paie = fheures * ftaux
    print("Le montant de la paie est de", paie)
