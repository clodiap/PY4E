import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


print("\n\n\n NEW\n")

counts = dict()
fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
print(counts)


print("\n\n\n NEW\n")


# Reading web pages

fhandle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhandle:
    print(line.decode().strip())
