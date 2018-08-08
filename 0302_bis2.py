HEURES_N = 40.0
TX_N = 1.0
TX_SUP = 1.5


#Calul de la paie en fonction du nb d'heures travaillées
def calcul_paie(heures_input, taux_input):
    if heures_input > HEURES_N :
        paiesup = (heures_input * taux_input) * TX_SUP
        print("Le montant de la paie est de", paiesup, "€")
    #sinon on garde le même taux
    else :
        paie = (heures_input * taux_input) * TX_N
        print("Le montant de la paie est de", paie, "€")

###############################


def user_input(txt_input) :
    error_input = True
    while error_input == True:
        val = input(txt_input)
        try :
            fval = float(val)
            error_input = False
            return fval
        except :
            error_input = True
            print("Il y a eu une erreur. Saisissez un nombre.")

heures = user_input("Combien d'heures travaillées ? ")
taux = user_input("À quel taux horaire ? ")

calcul_paie(heures, taux)
