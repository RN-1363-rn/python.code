# username =int( input("Enter a number: "))
# if username <=0:
#     print("incorrect username")
# elif username >0:
#     number = int(input("Enter a number: "))
#

# number = int(input("Enter a number: "))
# if number <=0:
#     print("erro")
# else:
#     for i in range(0,number+1,2):
#         print(i)




# numbers = []
# user_input = input("Enter a number(empty to quit): ")
# while user_input != "":
#     numbers.append(int(user_input))
#     user_input = input("Enter a number(empty to quit: ")
# printed_numbers = []
#
# for n in numbers:
#     if n >100 and n in printed_numbers:
#
#         printed_numbers.append(n)
#         print(n)



# Question 1
import random
dice_count = random.randint(1,6)
for i in range(dice_count):
    roll_dice = random.randint(1,6)