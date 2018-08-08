x = ("Glenn", "Sally", "Joseph")
print(x[2])

y = (1,9,2)
print(y)
print(max(y))

# tuples are not mutable

# we can also put a tuple on the left-hand side of an assignment statement
# we can even omit the parentheses

(a,b) = (4, "fred")
print(b)

(a,b) = (99,98)
print(a)

print("\n","--------"*20,"\n")

d = dict()
d["csev"] = 2
d["cwen"] = 4
for (k,v) in d.items() :
    print(k,v)

tups = d.items()
print(tups)

print("\n","--------"*20,"\n")

# tuples are comparable

print((0,1,2) < (5,1,2))
print((0,1,2000000) < (0,3,4))
print(("Jones", "Sally") < ("Jones", "Sam"))
print(("Jones", "Sally") > ("Adams", "Sam"))

print("\n","--------"*20,"\n")

# Sorting lists of tuples

##### Sorting by key
d = {"a":10, "b":1, "c":22}
print(d.items())
print(sorted(d.items()))

t = sorted(d.items())
print(t)

for k, v in sorted(d.items()):
    print(k,v)

print("\n","--------"*20,"\n")

##### sorting by value

c = {"a":10, "b":1, "c":22}
tmp = list()
for k, v in c.items():
    tmp.append( (v,k) )
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)
