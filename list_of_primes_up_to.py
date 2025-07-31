#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/30/2025
#Description: a function named list_of_primes_up_to that takes one integer argument - the limit - and returns a list of all primes up to and including the limit. The parameter should have a default argument of 100
def list_of_primes_up_to(limit=100):
    prime_list = [True] * (limit + 1)
    prime_list[0] = False
    prime_list[1] = False
    new_number = 2
    new_list = []
    while new_number < limit:
        list_position = 0
        for place in prime_list:
            if list_position % new_number == 0 and list_position != new_number:
                prime_list[list_position] = False
            list_position += 1
        new_number += 1
    new_list_position = 0
    for prime in prime_list:
        if prime:
            new_list.append(new_list_position)
        new_list_position += 1
    return new_list
