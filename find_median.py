#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 7/16/2025
#Description: accepts a list and returns the median of that list
def find_median(numbers):
    sorted = False
    while not sorted:
        place = 0
        vase = 1
        for i in numbers:
            if place+1 < len(numbers)-1:
                if numbers[place] > numbers[place +1]:
                    temp_storage = numbers[place+1]
                    numbers[place+1] = numbers[place]
                    numbers[place] = temp_storage
            else:
                if numbers[place] < numbers[place-1]:
                    temp_storage = numbers[place-1]
                    numbers[place-1] = numbers[place]
                    numbers[place] = temp_storage
            place += 1
        for i in numbers:
            if vase < len(numbers):
                if i > numbers[vase]:
                    break
            else:
                if vase == len(numbers):
                    if i >= numbers[vase-1]:
                        sorted = True
            vase += 1
    if len(numbers) % 2 == 1:
        median = numbers[int(len(numbers)/2)]
    else:
        median = (numbers[int(len(numbers) / 2)] + numbers[int(len(numbers) / 2)-1]) / 2
    return median


