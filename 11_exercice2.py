# Exercise 2: Write a program to look for lines of the form
# `New Revision: 39772`

# and extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average.

# Enter file:mbox.txt
# 38549.7949721

# Enter file:mbox-short.txt
# 39756.9259259
import re

fname = input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
hand = open(fname)

revision_list = list()
for lines in hand :
    lines = lines.rstrip()
    revision_numbers = re.findall("^New Revision: ([0-9]+)", lines)
    if len(revision_numbers) != 1 : continue
    inum = int(revision_numbers[0])
    revision_list.append(inum)

average = sum(revision_list) / len(revision_list)
print(average)

