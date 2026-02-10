# talent =float(input("enter your talent"))
# pound = float(input("enter your pound"))
# lot = float(input("enter your lot"))
# gra = float(input("enter your gra"))
#
#
# tal = talent*20*32*13.3
# po = pound* 32*13.3
# lo = lot* 13.3
# kilo = gra/1000
# print(tal)
# print(po)
# print(lo)
# print(kilo)
# import random
# code = str(random.randint(1,9))+ str(random.randint(0,6))
# user = input("Enter the cabin class : ")
# if user =="lux":
#     print("upper_desk cabin with a balcony")
# elif user == "A":
#     print("above the car desk with a window")
# elif user =="B":
#     print("below the car desk with a window")
# else:
#     print("wrong input")
# user = input("Enter your gender")
# if user == "male":
#     hem = input("Enter your hemoglobin value")
#     if "hem">"134" or "hem"<"167":
#         print("normal")
# if user == "female":
#     hem = input("Enter your hemoglobin value")
#     if "hem">"155" or "hem"<"117":
#         print("normal")
# user = int(input("Enter a year: "))
#            if user/4==400:
#                print("this year is leap year")
#            else:
#                print("this year is not leap year")
#  number= input("enter your number between (1_1000)")
# while number % "1000"==0:
#     print("it is good")
# else:
#     print("it is bad")
# i= 1
# while i <=1000:
#     print(i)
#     i+=1
from mdit_py_plugins.texmath.index import rules

# user = int(input("Enter a number:(cm) "))
# while user >1:
#     inch = user +2.5
#     print(inch)
# import random
# number = random.randint(1,10)
# while True:
#     guess = int(input("Enter an integer (0 to quit): "))
#     if guess == number:
#         print("You got it!")
#     if guess > number:
#         print("Your guess is too high")
#     elif guess < number:
#         print("Your guess is too low")
#     else:
#
# number = []
# numbers = int(input("Enter a number:(empty to quit): "))
# while True:
#     number.append(int(input("Enter a number:(empty to quit): ")))
#     print("smallest number:", number)
#     print("largest number:", number)
# password = "rules"
# username = "python"
# attempt = 0
# user = input("Enter your username: ")
# pas = input("Enter your password: ")
# if pas == password and user == username:
#     print("Welcome " )
# else:
#     print("Wrong username or password")
#     while attempt < 5:
#         attempt += 1
#
import mariadb
print(mariadb.__version__)
connection = mariadb.connect(
    host = "localhost",
    username = "root",
    password = "RN1363rn1363",
    database = "duckburg",
    port = 3306,)

print("connection established successfully")

# def get_employees_by_last_name(connection, last_name):
#     sql = "SELECT number ,last_name,first_name from  employees WHERE last_name =?"
#     cursor = connection.cursor()
#     cursor.execute(sql, (last_name,))
#     result = cursor.fetchall()
#     if result:
#         for a in result:
#             print(f"I am {a[2]}{a[1]}.My salary is {a[6]} euros per month")
#     else:
#         print(f" no record found with last name.'{last_name}'")
