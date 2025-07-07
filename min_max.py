#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/7/2025
#Description: Allows entry of a specified number of integers. Prints the smallest and largest entered values.
print("How many integers would you like to enter?")
minInteger = 0
maxInteger = 0
numberOfIntegers = int(input())
print("Please enter " + str(numberOfIntegers) + " integers.")
while numberOfIntegers > 0:
    temporaryInteger = int(input())
    if temporaryInteger > maxInteger : maxInteger = temporaryInteger
    if temporaryInteger < minInteger : minInteger = temporaryInteger
    numberOfIntegers -= 1
print("min: " + str(minInteger))
print("max: " + str(maxInteger))
