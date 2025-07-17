#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/16/2025
#Description: a function named add_surname that takes as a parameter a list of first names. It should use a list comprehension to return a list that contains only those names that start with a "K", but with the surname "Kardashian" added to each one, with a space between the first and last names.
def add_surname(names):
    namesAgain =[]
    for name in names:
        if name[0] == "K":
            namesAgain.append(name)
    station = 0
    for name in namesAgain:
        namesAgain[station] = namesAgain[station] + " Kardashian"
        station += 1

    return namesAgain