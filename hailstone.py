#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/11/2025
#Description: takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1
def hailstone(value):
    value = int(value)
    steps = 0
    while value != 1:
        if value % 2 == 0:
            value = even_hailstone(value)
        else:
            value = odd_hailstone(value)
        steps += 1
    return steps
def even_hailstone(value):
    value = value / 2
    return value
def odd_hailstone(value):
    value = (value * 3) + 1
    return value