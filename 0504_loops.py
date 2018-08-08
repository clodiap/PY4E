zork = 0
print("Before", zork)
for thing in [9,41,12,3,74,15] :
    zork = zork + 1
    print(zork, thing)
print("After", zork)


print("\n\n\n NEW\n")

zork = 0
print("Before", zork)
for thing in [9,41,12,3,74,15] :
    zork = zork + thing
    print(zork, thing)
print("After", zork)

print("\n\n\n NEW\n")

count = 0
sum = 0
print("Before", count, sum)
for value in [9,41,12,3,74,15] :
    count = count + 1
    sum = sum + value
    print (count, sum, value)
print("After", count, sum, sum / count)

print("\n\n\n NEW\n")

print("Before")
for value in [9,41,12,3,74,15] :
    if value > 20 :
        print("large number", value)
print("After")

print("\n\n\n NEW\n")

found = False
print("Before", found)
for value in [9,41,12,74,15] :
    if value == 3 :
        found = True
    print(found, value)
print("After",found)

print("\n\n\n NEW\n")

smallest_so_far = 100
print("Before", smallest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print("After", smallest_so_far)

print("\n\n\n NEW\n")

smallest_so_far = None # flag value
print("Before", smallest_so_far)
for value in [9,41,12,3,74,15] :
    if smallest_so_far is None :
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value
    print(smallest_so_far, value)

print("After", smallest_so_far)
