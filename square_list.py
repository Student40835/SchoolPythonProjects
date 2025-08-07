#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 8/6/2025
#Description: takes as a parameter a list of numbers and replaces each value with the square of that value
def square_list(list_in_question):
    int_start = 0
    for number in list_in_question:
        list_in_question[int_start]=number*number
        int_start+=1