# function
# create a function that prints "Welcome to Python"
# def welcome():
#     print("Welcome to Python")
# welcome()
#
# def add(a,b):
#     return a**b
# malik = add(3,4)
# print(malik)
from dictionary import average_score


# create a fubction that takes a name and print a greeting
# def greet(name):
#     print('Hello', name)
# greet('xyz')
#
#wrtite a function that returns the sum of two numbers
# def write(a,b):
#     return a+b
# print(write(20,20))

# # create a function that finds the largest of two numbers
# def largest(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(largest(25, 10))

# create a function that finds the smallest of two numbers
# def smallest(a,b):
#     if a < b:
#         return a
#     else:
#         return b
# print(smallest(2000,2))

# create a function that checks whether a number is even or odd
# def check(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# print(check(2))

# create a function that calculate the average of three numbers
# def average(a, b, c):
#     return(a + b + c) / 3
# print(average(10, 20, 30))

# lambda function
# square = lambda x: x ** 2
# print(square(7))

# write a lambda function that adds two numbers
# write = lambda a, b: a + b
# print(write(20,20))

# write a lambda function that multiplies two numbers
# write = lambda a, b: a * b
# print(write(1, 2))


# write a lambda function that divide two numbers
# write = lambda a, b: a / b
# print(write(1, 2))

# write a lambda function that subract two numbers
# write = lambda a, b: a - b
# print(write(1, 2))
#
# multiply every number in the list by 2
# num = [1,2,3,4,5]
# result = list(map(lambda x:x*2, num))
# print(result)

# Assignment
# # find square of a number
# square = lambda x: x * x
# print(square(4))

# #  create a lambda function that returns even or old
# even_old = lambda x: "even" if x % 4 == 0 else "odd"
# print(even_old(4))
# print(even_old(3))

# find largest number
# largest = lambda a, b, c, d, e: a if a > b else b if b > c else c if c > d else d if d > e else e if e > d else e
# print(largest(2, 5,7,12,22))

# file handling
# create and write to file
# file = open("score.txt", "w")
# file.write("Data analysis")
# file.close()

# read file content
# file = open("score.txt", "r")
# content = file.read()
# print(content)
# file.close()

# appending to a file
# file = open("score.txt", "a")
# file.write("\nWelcome to file handling")
# file.close()
#
# # create a file and write your name into it
with open("requirements.txt", "w") as file:
    file.write("Malik")

with open("malik.txt", "r") as file:
    print(file.read())
# # count number of  characters in a file
#
# with open("malik.txt", "r") as file:
#     content = (file.read())
# print(len(content))
