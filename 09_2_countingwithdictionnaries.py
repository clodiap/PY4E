ccc = dict()
ccc["csev"] = 1
ccc["cwen"] = 1
print(ccc)

ccc["cwen"] = ccc["cwen"] +1
print(ccc)

print("\n\n\n NEW\n")

# counts = dict()
# names = ["csev", "cwen","zqian", "cwen", "csev"]
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] += 1
# print(counts)

#GET
counts = dict()
names = ["csev", "cwen","zqian", "cwen", "csev"]
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


