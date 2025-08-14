#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 8/13/2025
#Description: a function named count_letters that takes a string as a parameter and returns a dictionary that tabulates how many of each letter is in that string
def count_letters(string_in_question):
    letter_dictionary = {}
    letter_list = []
    string_in_question = string_in_question.lower()
    for letter in string_in_question:
        if letter != letter.upper():
            letter_list.append(letter.upper())
    letter_set=set(letter_list)
    for letter in letter_set:
            letter_dictionary[letter] = 0
    for letter in letter_list:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
    return letter_dictionary
