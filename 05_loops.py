
n = 5
while n > 0 :
    print(n)
    n = n - 1
print("Blastoff!")
print(n)

print("\n\n\n NEW\n")

while True:
    line = input("Type 'done' >")
    if line == "done" :
        break
    print(line)
print("done")

print("\n\n\n NEW\n")

while True:
    line = input(">")
    if line[0] == "#" :
        continue
    elif line == "done" :
        break
    print(line)
print("done!")

