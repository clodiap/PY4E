fname = input("Enter file: ")
if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip()
    wds = line.split()

    for w in wds :
        #if the key not there the count is zero
        # oldcount = di.get(w,0)
        # print(w,"old", oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount

        #idiom : retrieve / create / update counter
        di[w] = di.get(w, 0) + 1

        # if w in di :
        #     di[w] = di[w] + 1
        # else:
        #     di[w] = 1

# print(di)

# now we want to find the most commun word
largest = -1
theword = None
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = k #capture / remember that was largest

print(theword,largest)
