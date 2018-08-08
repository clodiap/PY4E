abc = "with three words"
stuff = abc.split()
print(stuff)
print (len(stuff))
print(stuff[0])

print(stuff)
for w in stuff:
    print(w)


print("\n\n\n NEW\n")

line = "A lot                 of spaces"
etc = line.split()
print(etc)

print("\n\n\n NEW\n")

line = "first;second;third"
thing = line.split()
print(thing)

print(len(thing))

thing = line.split(";")
print(thing)
print(len(thing))

print("\n\n\n NEW\n")

fhand = open("mbox-short.txt")
for ligne in fhand:
    ligne = ligne.rstrip()
    if not ligne.startswith("From") : continue
    words = ligne.split()
    emails = words[1]
    print(emails)
    pieces = emails.split("@")
    print(pieces[1])

fruit = "Banana"
fruit[0] = "b"
print(fruit)
