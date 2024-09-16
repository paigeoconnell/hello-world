# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:56:08 2024

@author: oamin
"""

# Question 1: Print "Hello, Spyder" in the console.

print("Hello Spyder")

# Question 2: Print the result of 5 + 3 in interactive mode vs. in a script.

print(5+3)



# Question 3: Ask for a user's name and print a greeting.

name = input("input your name here:")
print("hello," + name)

# Question 4: Store the number 10 in a variable and print it.

number = 10
print(number)


# Question 5: Calculate and print the product of 7 and 8.

print(7*8)


# Question 6: Show the difference between adding numbers and adding strings.


# Adding numbers
print(5+6)

# Adding strings

print("5" + "6")

# Question 7: Convert the string "123" to an integer and add 7 to it.

number = "123"
number = int(number)
print(number + 7)

# Question 8: Calculate the area of a rectangle from user input.

width = float(input("input width :"))
length = float(input("input length: "))
area = length * width
print(area)

# Calculate total interest to be paid on a student loan over the course of a loan period

#          Total Interest = Principal * (annual rate / 100) * years
principal = float(input("input principal"))
annualrate = float(input("input annualrate"))
years = float(input("input years"))
totalinterest = principal * (annualrate / 100) * years
print(totalinterest)
