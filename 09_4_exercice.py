# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

file = open(name)

list_emails = list()

for lines in file : #création d'une liste d'emails
    if not lines.startswith("From ") : continue
    words = lines.split()
    list_emails.append(words[1])

count_emails = dict()

# transformation de la liste en dictionnaire, avec l'email et le nb de fois où il apparait
for emails in list_emails:
    count_emails[emails] = count_emails.get(emails,0) + 1

# largest_num = None
largest_num = -1
max_emails = None

for kkk,vvv in count_emails.items(): #maximum loop
    if vvv > largest_num :
        largest_num = vvv
        max_emails = kkk

    # if largest_num == None:
    #     largest_num = vvv
    #     max_emails = kkk
    # elif largest_num < vvv :
    #     largest_num = vvv
    #     max_emails = kkk

print(max_emails, largest_num)
