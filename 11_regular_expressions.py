# hand = open("mbox-short.txt")
# for line in hand:
#     line = line.rstrip()
#     if line.find("From:") >= 0:
#         print(line)

# import re


# hand = open("mbox-short.txt")
# for line in hand:
#     line = line.rstrip()
#     if re.search("From:", line):
#         print(line)

# hand = open("mbox-short.txt")
# for line in hand:
#     line = line.rstrip()
#     if line.startswith("From:"):
#         print(line)

import re

hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line)

x = "My 2 favorite numbers are 19 and 42"
y = re.findall("[0-9]+", x)
print(y)

y = re.findall("[AEIOU]+",x)
print(y)

# [0-9] --> single digit
# + --> at list 1

# greedy matching --> * + match the largest possible string
# ^F.+: --> first character is an F, one or more character (.+), last character is a :

x = "From: Using the : character"
y = re.findall("^F.+:", x)
print(y)

# non-greedy matching --> ? with the question mark it is less greedy

y = re.findall("^F.+?:", x)
print(y)

# Fine-tuning string extraction
# \S+ --> at least one non-whitespace character
# \S --> non-whitespace character

x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("\S+@\S+", x)
print(y)

# parentheses are not part of the match, but they tell where to start and stop what string to extract
# y = re.findall('^From (\S+@\S+',x)
print(y)

data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print(atpos)
sppos = data.find(" ",atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

# [^ ] --> match non-blank character
# * --> match many of them
lin = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("@([^ ]*)", lin)
print(y)

# ^From --> starting at the beginning of the line, look for the string "From"

y = re.findall("^From .*@([^ ]*)",lin)
print(y)

# Spam Confidence
# looking for numbers after the text « X-DSPAM-Confidence: »

hand = open("mbox-short.txt")
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print("Maximum:", max(numlist))

# Escape character
# \$ --> a real dollar sign
# [0-9.] --> a digit or period
# + --> at least one or more

x = "We just received $10.00 for cookies."
y = re.findall("\$[0-9.]+",x)
print(y)
