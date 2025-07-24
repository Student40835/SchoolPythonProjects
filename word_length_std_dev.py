#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/23/2025
#Description:  a function called word_length_std_dev that takes as a parameter a string and returns the sample standard deviation of the lengths of the words in that string
def word_length_std_dev(sentence):
    word_list = sentence.split()
    number_of_letters = 0
    for word in word_list:
        number_of_letters += len(word)
    average_length_of_a_word = number_of_letters / len(word_list)
    if len(word_list) > 1:
        standard_deviation = 0
        for word in word_list:
            standard_deviation += (len(word)-average_length_of_a_word)**2
        standard_deviation = standard_deviation/len(word_list)
        standard_deviation = standard_deviation ** 0.5
    else:
        standard_deviation = 0
        print("Sentence is too short")
    return standard_deviation