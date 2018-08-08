# Exercise 1: [wordlist2]

# Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

filename = input("Enter a file: ")
if len(filename) < 1 : filename = "words.txt"

file = open(filename)

dictionnaire = dict()

for lines in file :
    lines = lines.rstrip()
    # for words in lines :
    words = lines.split()

    for word in words :
        dictionnaire[word] = dictionnaire.get(word, 0) + 1

print(dictionnaire)
