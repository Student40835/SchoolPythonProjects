def measure_string(s):
     """returns the length of the string s"""
     count = 0
     for letter in s:
         count += 1
     return count

def measure_user_string():
    """returns the length of a string entered by the user"""
    my_string = input("enter a string:")
    string_length = measure_string(string)
    return string_length

measure_user_string()