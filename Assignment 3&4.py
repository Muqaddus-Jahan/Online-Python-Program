#ASSIGNMENT 3

#Question 1:Write a python program to print a following string in a specific format

#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#Question 2:Write a python program to get the python version you are using

# import sys
# print("Python version")
# print (sys.version)
# print (sys.version_info)

#Question 3:Write a python prgram to display the current date and time

# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Question 4:Write a python program which accepts the radius of a circle from the user and compute the area

# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

#Question 5:Write a python program which accepts the user's first and last name and print them in reverse order with a space between them

# first_name = input("Please enter first name:")    
# last_name = input("Please enter last name:")    
# print (last_name+" "+first_name)

#Question 6:Write a python program which takes two inputs from user and print them addition

# num_1 = int(input('Enter your first number: '))
# num_2 = int(input('Enter your second number: '))

# # Addition
# print('{} + {} = '.format(num_1, num_2))
# print(num_1 + num_2)

#Question 7:Write a python program which takes five inputs from user for different subjects marks, total it and generate mark sheet using grades

# mark1 = int(input("Enter the first subject marks"))
# mark2 = int(input("Enter the second subject marks"))
# mark3 = int(input("Enter the third subject marks"))
# mark4 = int(input("Enter the fourth subject marks"))
# mark5 = int(input("Enter the fifth subject marks"))

# total = mark1 +mark2 +mark3 +mark4 +mark5
# avg = total/5

# if avg>=91 and avg<=100:
#     print("Your Grade is A+")
# elif avg>=81 and avg<91:
#     print("Your Grade is A")
# elif avg>=71 and avg<81:
#     print("Your Grade is B+")
# elif avg>=61 and avg<71:
#     print("Your Grade is B")
# elif avg>=51 and avg<61:
#     print("Your Grade is C+")
# elif avg>=41 and avg<51:
#     print("Your Grade is C")
# elif avg>=33 and avg<41:
#     print("Your Grade is D")
# elif avg>=21 and avg<33:
#     print("Your Grade is E")
# elif avg>=0 and avg<21:
#     print("Your Grade is F")
# else:
#     print("Invalid Input!")

#Question 8:Write a python program which take input from the user and identify that the given number is even or odd# num = int(input ('Enter any number to test whether it is odd or even: '))

# if (num % 2) == 0:
#        print ("The number is even")
# else:
#        print ("The provided number is odd")

#Question 9:Write a program which print the length of the list

# list = ["Muqaddus", "Cat", "Lion", "Parrot",10, 20, 30,]
# n = len(list)
# print("The length of list is: ", n)

#Question 10:"Write a python program to sum all the numeric items in a list

# list = [10, 22, 30, 45, 65, 78, 91]
# n = sum(list)
# print("The sum of numeric items in list is: ", n)

#Question 11:Write a python program to get the largest number from a numeric list

# list = [10, 22, 30, 45, 65, 78, 91]
# n = max(list)
# print("The largest number in list is: ", n)

# Question 12:Take a list, say for example this one:
# a=[1,1,2,3,5,8,13,21,34,55,89]
# Write a program that prints out all the elements of the list that are less than 5

# a=[1,1,2,3,5,8,13,21,34,55,89]
# for i in a:
#     if i < 5:
#         print(i)

# ASSIGNMENT 4
#Question 1: Make a calculator using python with addition, subtraction, multiplication, division and power

# num_1 = int(input('Enter your first number: '))
# num_2 = int(input('Enter your second number: '))

# # Addition
# print('{} + {} = '.format(num_1, num_2))
# print(num_1 + num_2)

# # Subtraction
# print('{} - {} = '.format(num_1, num_2))
# print(num_1 - num_2)

# # Multiplication
# print('{} * {} = '.format(num_1, num_2))
# print(num_1 * num_2)

# # Division
# print('{} / {} = '.format(num_1, num_2))
# print(num_1 / num_2)

# #Power
# print('{} ^ {} = ' .format(num_1, num_2))
# print(num_1 ** num_2)

#Question 2:Write a program to check if there is any numeric value in list using for loop

# list=[ '1', '6', '3', '5', '3', '4', 'crow', 'parrot', 'eagle']
# i=input('enter the data to check')
# if i in list:
#     print("exist")
# else:
#     print("not exist")
    
#Question 3: Write a python script to add a key to a dictionary

# data = {10, 20, 30, 40, 50}
# print(data)
# data.update({2, 35})
# print(data)

#Question 4: Write a python program to sum all the numeric items in a dictionary

# my_dict = [100,254,247,789]
# print(sum(my_dict))

#Question 5: Write a python program to identify duplicate values from the list

# list=[1,2,3,4,5,2,3,4,7,9,5,11,67,45,97,11,45,'cat','lion','dog','lion']
# list1=[]
# for i in list:
#     if i not in list1:
#         list1.append(i)
#     else:
#         print(i,end=' ')

#Question 6: Write a python program to check if a given key already exists in a diictionary

# data = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#   if x in data:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present(10)
# is_key_present(9)


