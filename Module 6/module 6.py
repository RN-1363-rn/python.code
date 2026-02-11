# Exam 1

import random

def roll_dice():
    return random.randint(1,6)

result = 0
while  result !=6:
    result = roll_dice()
    print(result)
    if result == 6:
        break


# Exam 2


import random

def roll_dice(sides):
    return random.randint(1,sides)

sides = int(input("Enter number of sides: "))
result = 0
while result !=sides:
    result = roll_dice(sides)
    print(result)


# Exam 3

def gallons_to_liters(gallons):
    return int(gallons * 0.45)
while True :
    gallons = int(input("Enter number of gallons: "))
    if gallons == 0:
        break



# Exam 4

def sum_list(number):
    return sum(number)

my_list = [1,2,3,4,5,7]

result = sum_list(my_list)

print(result)


#Exam 5

def remove_even(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

original_list = [1,2,3,4,5,7]
filtered_list = remove_even(original_list)
print(filtered_list)
print(original_list)


# Exam 6
import random
def