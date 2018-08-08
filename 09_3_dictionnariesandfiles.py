counts = dict()
print("Enter a line of text: ")
# line = input("")
line = "The clown ran after the car ran into the tent and the ten fell down on the clown and the car"

words = line.split()
print("Words:", words)

print("counting…")
for word in words:
    counts[word] = counts.get(word,0) + 1
print("counts", counts)

print("list(counts):",list(counts))

print("counts.keys()", counts.keys())

print("counts.values()", counts.values())

print("counts.items()", counts.items())

print("\n\n\n NEW\n")


jjj = { "Chuck" : 1 , "fred" : 42, "jan" : 100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)
