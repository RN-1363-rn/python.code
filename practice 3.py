# age = int(input("Enter age: "))
# if 15 <= age < 18:
#     weight = float(input("Enter weight (kg): "))
# if (age >=18 or age>=15 and weight >=55):
#     print("The medicine can be used.")
# age = int(input("Enter age: "))
# if 15 <= age < 18:
#     weight = float(input("Enter weight (kg): "))
# if (age >=18 or age>=15 and weight >=55):
#     print("The medicine can be used.")
# else:
#     print("The medicine cannot be used.")
#
# age = int(input("Enter your age: "))
# if age>=18:
#     print("You can vote.")
# elif age<18:
#     print("You can not vote.")
# else:
#     different = 18- age
#     print (f"You are a small child.")
from networkx.algorithms.operators.binary import difference

# consumption = float(input("Enter your favorite number: "))
# if consumption <= 50:
#     print (" bill cost is 0.1")
# elif consumption >200 :
#     print ("bill cost is 0.8")
# elif consumption >50 or consumption >200:
#     print ("bill cost is 0.6")
# else:
#     print ( "finnish")
# physical_score = int(input("Enter your physic grade: "))
# math = int(input("Enter your math grade: "))
# chemistry_score = int(input("Enter your chemistry grade: "))
# if physical_score  <=50 or math <= 50 or chemistry_score <= 50 :
#     print ("your score is too low")
# elif chemistry_score >= 95 :
#     print (" you can give scholarship")
# elif physical_score >=90 and math >=90 :
#     print (" you can give scholarship")
# else:
#     print (" you can  not give scholarship")
# score = int(input("Enter your score: "))
# if score >= 90:
#     print("Your score is good")
# elif score < 50:
#     print("Your score is bad")
# elif score >= 50 or score < 90 :
#     print("Your score is better")
# else:
#     print(" good lock")
#
# Exercise 1
length = int(input("Enter the length of fish (cm): "))
if length < 42 :
    difference = 42 - length
    print(f"Fish is {difference} cm. you back into the lake.")
else :
    print ("you got it")

# Exercise 2
cabin_class = input("Enter the cabin class:")
if cabin_class == "lux":
    print("upper desk cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car desk, equipped with a window")
elif cabin_class == "B":
    print("Windowless cabin above the car desk.")
elif cabin_class == "C":
    print("Windowless cabin below the car desk.")
else:
    print("Cabin not recognized.")

#Exercise 3
gender = input("Enter your  gender (m/f: ")
hemoglobin = int(input("Enter the hemoglobin:"))
if gender == "f":
    if hemoglobin < 155 or hemoglobin > 117:
        print("hemoglobin is normal")
elif gender == "m":
    if hemoglobin < 167 or hemoglobin > 134:
        print("hemoglobin is normal")
else:
    print("hemoglobin not recognized.")

#Exercise 4
year = int(input("Enter the year:"))
if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
    print("leap year")
else:
    print("not leap year")

