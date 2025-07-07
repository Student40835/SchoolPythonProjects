#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/7/2025
#Description: lists the factors of an entered integer
print("Please enter a positive integer: ")
integer = int(input())
factor = 1
print("The factors of " + str(integer) + " are:")
while factor <= integer:
    if integer % factor == 0: print(str(factor))
    factor += 1