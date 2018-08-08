# The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:

# Why should you learn to write programs? 7746
# 12 1929 8827
# Writing programs (or programming) is a very creative
# 7 and rewarding activity.  You can write programs for
# many reasons, ranging from making your living to solving
# 8837 a difficult data analysis problem to having fun to helping 128
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program ...

# The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re

# fname = input("Enter file: ")
# # if len(fname) < 1 : fname = "regex_sum_42.txt"
# if len(fname) < 1 : fname = "regex_sum_90810.txt"
# hand = open(fname)

hand = open("regex_sum_90810.txt")

thenumlist = list()
for lines in hand :
    lines = lines.rstrip()
    thenumbers = re.findall("[0-9]+", lines)
    if len(thenumbers) == 0 : continue
    # print(thenumbers)

    for i in thenumbers :
        i = int(i)
        # print(i)
        thenumlist.append(i)
        # print(thenumlist)
print("The sum is:", sum(thenumlist))
print(len(thenumlist))


# Optional: Just for Fun

# There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:

# Python 2
# import re
# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

# Python 3:
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

# Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework. List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.
