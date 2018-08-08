fname = input("Enter file: ")
if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip()
    line = line.lower()
    wds = line.split()

    for w in wds :
        for letters in w:
            if letters.isalpha() and len(w) > 3:
                di[w] = di.get(w, 0) + 1

# print(di)

tmp = list()
for k,v in di.items():
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)

# print(tmp)

tmp = sorted(tmp, reverse=True)
# print("sorted", tmp[:5])

for v,k in tmp[:100]:
    print(k,v)

# x = sorted(di.items())
# print(x[:5])
