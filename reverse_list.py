#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 8/6/2025
#Description: takes as a parameter a list and reverses the order of the elements in that list
def reverse_list(list_in_question):
    int_start = -1
    list_out_of_the_question = []
    for number in list_in_question:
        list_out_of_the_question.append(number)
        int_start+=1
    for number in list_out_of_the_question:
        list_in_question[int_start]=number
        int_start-=1