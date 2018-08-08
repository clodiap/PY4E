#lists are mutable
#strings are not mutable

lotto = [2,14,20,41,63]
print(lotto)
lotto[2] = 28
print(lotto)


print("\n\n\n NEW\n")

greet = "Hello Bob"
print(len(greet))

x = [1,2,"joe",99]
print(len(x))

print("\n\n\n NEW\n")

friends = ["Joseph", "Glenn", "Sally"]
for friend in friends :
    print("Happy New Year:", friend)

for i in range(len(friends)):
    friend = friends[i]
    print("Happy New Year:", friend)

