#concatenating lists using +

a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)
print(a)

print("\n\n\n NEW\n")

t = [9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

print("\n\n\n NEW\n")

stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)
stuff.append("cookie")
print(stuff)

print("\n\n\n NEW\n")

friends = ["Joseph", "Glenn", "Sally"]
friends.sort()
print(friends)
print(friends[1])

print("\n\n\n NEW\n")

nums = [9,41,12,3,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

print("\n\n\n NEW\n")

numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/len(numlist)
print("Average:", average)
