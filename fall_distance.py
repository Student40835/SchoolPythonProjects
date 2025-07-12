#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/11/2025
#Description: a function that takes a given amount of seconds and converts it into a distance fallen with earth's gravity
def fall_distance(seconds):
    distance = ((1/2) * 9.8 * (seconds * seconds))
    return distance