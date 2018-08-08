x = 25
if x < 10:
    print("smaller than 10")
if x > 20:
    print("bigger than 10")

print("finished\n\n\n")

##############################

x = 5

for i in range(5) :
    print(i)
    if i > 2 :
        print("bigger than 2")
    print("Done with i", i)

print("all done\n\n\n")

##############################

chiffre = input("entrer un chiffre : ")

try :
    chiffre = int(chiffre)
except :
    chiffre = -1

if chiffre == -1:
    print("qu'est-ce que tu n'as pas compris ?")
    chiffre2 = input("essaie encore : ")
    try :
        chiffre2 = int(chiffre2)
    except :
        chiffre2 = -1

    if chiffre2 == -1 :
        print("visiblement tu es un peu dur à la comprenette, j'abandonne !")
    else :
        print(chiffre2, "fois bravo, tu as enfin compris, tout n'est pas perdu !!!")
else :
    print(chiffre, "fois bravo, tu as compris la question !!!")
