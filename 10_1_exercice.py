# Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

name = input("enter a file: ")
if len(name) < 1 : name = "mbox-short.txt"
file = open(name)

list_emails = list()

for lines in file :
    lines = lines.rstrip()
    if not lines.startswith("From "): continue
    words = lines.split()
    list_emails.append(words[1])

# print(list_emails)

count_emails = dict()

for emails in list_emails :
    count_emails[emails] = count_emails.get(emails, 0) +1

# print(count_emails)

tmplist = list()

for key, val in count_emails.items():
    newtup = (val,key)
    tmplist.append(newtup)

tmplist = sorted(tmplist, reverse = True)

max_emails = max(tmplist)

print(max_emails[1], max_emails[0])

