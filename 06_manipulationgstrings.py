fruit = "banana"
if "a" in fruit :
    print("Found it!")

print("\n\n\n NEW\n")

greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(greet)
print("Hi THERE".lower())

print("\n\n\n NEW\n")

pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)

print("\n\n\n NEW\n")

nstr = greet.replace('o','x')

greet = "Hello Bob"
nstr = greet.replace("Bob", "Jane")
print(nstr)
nstr = greet.replace("o","X")
print(nstr)

print("\n\n\n NEW\n")

greet = "   Hello   "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

print("\n\n\n NEW\n")

line = "Please have a nice day"
print(line.startswith("Please"))
print(line.startswith("p"))

print("\n\n\n NEW\n")

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find("@")
print(atpos)

sppos = data.find(" ", atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)
