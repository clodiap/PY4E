def thing():
    print("hello")
    print("Fun")

thing()
print("Zip")
thing()

print("\n\n\n NEW\n")

big = max("Hello world")
print(big)
tiny = min("Hello world")
print(tiny)

print("\n\n\n NEW\n")

print (float(99) / 100)

i = 42
type(i)

f = float(i)
print(f)

type(f)
print(1 + 2 * float(3) / 4 - 5)

print("\n\n\n NEW\n")
# input always gives us a string
sval = '123'
type(sval)
# print(sval + 1)

ival = int(sval)
type(ival)
print(ival + 1)

# nsv = 'hello bob'
# niv = int(nsv)

print("\n\n\n NEW\n")


def greet(lang):
    if lang == 'es' :
        print('Hola')
    elif lang == 'fr' :
        print('Bonjour')
    else :
        print('Hello')

greet('en')
greet('es')
greet('fr')

print("\n\n\n NEW\n")

def greet2():
    return "Hello"

print(greet2(), "Glenn")
print(greet2(), "Sally")

print("\n\n\n NEW\n")

def greet3(lang):
    if lang == 'es':
        return 'Hola'
    elif lang =='fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet3("en"), "Glenn")
print(greet3("es"), "Sally")
print(greet3("fr"), "Michael")

print("\n\n\n NEW\n")

def addtwo(a,b):
    added = a + b
    return added
x = addtwo(3,5)
print(x)

print("\n\n\n NEW\n")

import random

for i in range(10):
    x = random.random()
    print(x)


print("\n\n\n NEW\n")

x = random.randint(5,10)
print(x)
y = random.randint(5,10)
print(y)

print("\n\n\n NEW\n")

t = [1, 2, 3]
random.choice(t)
print(random.choice(t))
