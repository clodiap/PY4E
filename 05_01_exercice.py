"""Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number."""


# number = None
# while number != "done" :
#     number = input("Enter a number: ")
#     print(number)
#     if number != "done":
#         try:
#             inumber = int(number)
#             list_inumber = [inumber]
#         except :
#             print("Invalid input")

# print(inumber)
# print("done")

num = 0
tot = 0.0

while True :
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try:
        fval = float(sval)

    except:
        print("Invalid input")
        continue
    num = num + 1
    tot = tot + fval
    # print(num, tot)

# print("all done")
print(tot, num, tot/num)

