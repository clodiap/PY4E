# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
# Sample Execution:
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter a file: ")
if len(name) < 1 : name = "mbox-short.txt"

file = open(name)
time = list()

for lines in file :
    lines = lines.rstrip()
    if not lines.startswith("From ") : continue

    words = lines.split()
    hours = words[5]
    new_hours = hours.split(":")
    # time = new_hours[0]
    time.append(new_hours[0])

# print(time)

count_hours = dict()

for i in time :
    count_hours[i] = count_hours.get(i,0) + 1
# print(count_hours)

hourlist = list()

# for key, value in count_hours.items():
#     newtup = (key, value)
#     hourlist.append(newtup)
# hourlist = sorted(hourlist)

hourlist = sorted( [ (k,v) for k,v in count_hours.items() ] )

# print(hourlist)

for k, v in hourlist:
    print(k,v)
