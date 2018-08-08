 # Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters "done". Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

list_numbers = list()

while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    else:
        try:
            user_input = int(user_input)
        except:
            print("not a number")
            continue

        list_numbers.append(user_input)

# print("Done!")
print(list_numbers)
print("max number = ", max(list_numbers))
print("min number = ", min(list_numbers))



