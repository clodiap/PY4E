# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

name = input("Enter a file: ")
if len(name) < 1 : name = "mbox-short.txt"

file = open(name)

list_domains = list()

for lines in file :
    if not lines.startswith("From "): continue
    words = lines.split()
    domains = words[1].split("@")
    list_domains.append(domains[1])

count_domains = dict()

for i in list_domains:
    count_domains[i] = count_domains.get(i, 0) + 1

print(count_domains)
