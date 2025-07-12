#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/11/2025
#Description: returns the value of a specific position of the fibonacci sequence
def fib(position):
    position = int(position)
    value = 1
    last_value = 0
    temporary_value = 0
    if position == 0:
        return 0
    while position > 1:
        temporary_value = value
        value = last_value + value
        last_value = temporary_value
        position-=1
    return value