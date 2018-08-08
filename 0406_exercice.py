"""Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function. """

NORMAL_RATE = 1
SUP_RATE = 1.5

def computepay(hours,rate):
    if hours <= 40.0:
        pay = hours * (rate * NORMAL_RATE)
        return pay
    if hours > 40.0:
        pay = (40 * (rate * NORMAL_RATE)) + ((hours - 40) * (rate * SUP_RATE))
        return pay

hrs = input("Enter Hours:")
user_rate = input("Enter Rate:")

hrs = float(hrs)
user_rate = float(user_rate)

p = computepay(hrs,user_rate)

print("Pay",p)


