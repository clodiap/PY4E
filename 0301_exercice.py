TX_N = 1
TX_SUP = 1.5

heures = input("Combien d'heures travaillées ? ")
taux = input ("À quel taux horaire ? ")

#transformation en float
fheures = float(heures)
ftaux = float(taux)

# si heures travaillées > 40, le taux horaire est multiplié par 1.5
if fheures > 40 :
    paie = 40 * (ftaux * TX_N)
    paiesup = paie + (fheures - 40) * (ftaux * TX_SUP)
    print("Le montant de la paie est de", paiesup)
#sinon on garde le même taux
else :
    paie = fheures * (ftaux * TX_N)
    print("Le montant de la paie est de", paie)
