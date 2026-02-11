
#practice 1


import random
dice_count = random.randint(1,6)
print(dice_count)
total = random.randint(1,6)
print(total)
sum = total + dice_count
print(sum)

#practice 2

numbers =[]
user_input = input("Enter a number(empty to quit): ")
while user_input != "":
    numbers.append(user_input)
    user_input = input("Enter another number(empty to quit: ")

numbers.sort(reverse=True)  # sorts the list into descending order

print("top 5 numbers:")
for i in range(5):
    print(numbers[i]) # print the first 5 numbers (the largest 5 numbers)


#practice 3

user_input = input("Enter a number(empty to quit): ")
if user_input == "number":
    print("number")
else:
    print("wrong input")


#practice 4

cities= []
for i in range(5):
    name = input("Enter a city name: ")
    cities.append(name)
for city in cities:
    print(cities)

