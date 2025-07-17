#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/16/2025
#Description: returns a list with duplicates removed
def without_duplicates(list_with_duplicates):
    list_without_duplicates = []
    for item in list_with_duplicates:
        if item not in list_without_duplicates:
            list_without_duplicates.append(item)
    return list_without_duplicates
