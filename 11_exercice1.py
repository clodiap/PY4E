# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author

# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-

# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4218 lines that matched java$

# récupérer les lignes, les lire, faire une liste avec la regular expression, compter combien d'items dans la liste

import re

re_user = input("Enter a regular expression: ")
if len(re_user) < 1 : re_user = "^Author"

hand = open("mbox.txt")
re_list = list()
for line in hand :
    line = line.rstrip()
    stuff = re.findall(re_user, line)
    if len(stuff) == 0 : continue
    # print(stuff)
    re_list.append(stuff)
print("mbox.txt had", len(re_list), "lines that matched", re_user)
