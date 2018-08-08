fname = input("Enter file: ")
if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip()
    wds = line.split()

    for w in wds :
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

for v,k in tmp[:5]:
    print(k,v)

# x = sorted(di.items())
# print(x[:5])
