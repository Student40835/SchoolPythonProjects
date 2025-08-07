#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 8/6/2025
#Description: a recursive function named multiply that takes two positive integers as parameters and returns the product of those two numbers
number_3=0
def multiply(number_one,number_2):
    if number_2 == 0:
        return 0
    if number_2 == 1:
        return number_one
    if number_2 >= 2:
        return number_one + multiply(number_one,number_2-1)