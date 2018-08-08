# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.

name = input("Enter a file: ")
if len(name) < 1 : name = "romeo.txt"
file = open(name)


# Création d'une liste de lettres
letterlist = list()
for lines in file :
    lines = lines.rstrip()
    lines = lines.lower()
    for letters in lines :
        if letters.isalpha():
            letterlist.append(letters)

# Dictionnaire avec les lettres et le nombre de fois où elles apparaissent
count_letters = dict()
for i in letterlist :
    count_letters[i] = count_letters.get(i,0) + 1

# Les afficher dans l'ordre décroissant (du plus utilisé au moins utilisé)
letterorder = list()
letterorder = sorted( [(v,k) for k,v in count_letters.items()], reverse = True)

for v , k in letterorder:
    print(k, v)
