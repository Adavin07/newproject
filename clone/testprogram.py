# take a list any value find out the second largest value

# list1 = [45, 35, 54, 60]
# list1.sort()
# print(list1)
# print(list1[-2])

# take my name and find out the each character

# name = {"nam": "edwin"}
#
# each_character = name["nam"]
#
# print(each_character)
# # i = 0
# for i in each_character:
# #     print(each_character)
#
# # nested if else1
#
# percentage = eval("enter your percentage")
#
# if percentage < 0 and percentage > 100:
#     print("percentage you have entered is not valid")
#     if percentage >= 35:
#         print("just pass")
#     elif percentage <= 50:
#         print("second class")
#
#     elif percentage >=75:
#         print("first class")
# else:
#     print("you are fail")
#
# x = y = z = e = 10
# print(y)

# Take two int values from user and print greatest among them.

# A python program to accept a string from keyboard and display it.
# a = input('enter anything')
# print(a)
# a python program to accept a character as a string
# a = input("enter anything ")
# print("YYYH:"+a)

# # PYTHON PROGRAM TO ACCEPT A SINGLE CHARACTER FROM  KEYBOARD
# a = input("enter a single character ")
# print(a[0])

# a python program to accept an integer number from keyboard
#
# # a python program to accept two numbers and find their sum
# a = int(input('first integer '))
# b = int(input('second integer '))
# print("the value of a and b ", a + b)
# # print(f"the value of {a} and {b}", a + b)
#
# # a python program to find sum and product of two numbers.
# a = int(input('first integer ')),
# b = int(input('second integer '))
# print('the sum of {2} and {0} is {1}'.format(a, b, a * b))

# write a python program to accept 3 integers in same line and give output
# var1, var2, var3 = [int(x) for x in input(" enter three numbers ").split('+')]
# print('sum', var1+var2+var3)

# write a program to evaluating an expression entered from keyboard

# a = eval(input('enter an expression :'))
# print("%s"%a)
#
# a = 1
# if a == 1:
#     print("one")

# write a program to display a group of message when the condition is true

# a = "edwin is good boy"
# b = a
# if a == b:
#     print(a)
#     print('subash is a bad boy')

# a = 'subash'
# b = 'edwin'
# c = a
# a = b
# b = c
# print(a)
# print(b)

# a = 1234567
# print(str(a)[::-1])
#

# a python program to test whether a given number is in between 1 and 10

# b = int(input("enter any number 1 and 10 "))
# if b > 0 and b <= 10 :
#     print("entered number is between 1 and 10")
# else:
#     print("it is not present")

# a python program to know if a given number is zero, positive or negative.
# a = int(input('enter any number '))
# if a < 0:
#     print('it is negative number')
# elif a > 0:
#     print('it is positive number')
# else:
#     print("it is equal")

# write a program to reverse a string in program
# a = "edwin"
# print(a[::-1])

# Write a program to count the number of letters in a word.
# a = "pythonlobby"
# print(len(a))

# write We are given a string and we need to reverse words of a given string
# a = " geeks quiz practice code"
# b = a.split()[::-1]
# l =[]
# for i in b:
#     l.append(i)
# print(l)
# print(" ".join(l))


# given a positive number return the square root of it , if the number is not a perfect return the floor of its
# square root
#
# import math
# square_root = int(input('enter the number '))
# if square_root > 0:
#     print(math.sqrt(square_root))
# else:
#     print("Enter valid number")


# Find the length of a string
# # a = "edwin"
# print(len(a))

# # find using for loop
# def getlen(str):
#     counter = 0
#     for i in str:
#        counter += 1
#     return counter
# print(getlen('edwin'))

# str = 'edwin'
# count = 0
# for i in str:
#     count += 1
# print(count)

# by using join method
# str = "edwin"
# random = "x"
# print((random).join(str))
# print((random).join(str).count(random)+1)

# Count characters in string
# str = 'edwin'
# print(str.count('e'))

# using for loop using count method
# str = 'edwine francies'
# list1 = []
# for i in str:
#     if i not in list1:
#         list1.append(i)
#         print(i, 'occured', str.count(i), 'times')

# string slicing
# a = "edwin"
# print(a[1:6:2])

# # do slicing using for loop
# a = 'francis'
# for i in a[1:4:2]:
#     print(i)

# replace first occurance
# a = 'edwin francies'
# print(a.replace('e', 'd', 1))

# using for loop replace first occurance
# a = 'hi my name is edwin \n and edwin is very good boy'
# print(a)
# print(a.replace('edwin', 'vicky'))
# a = ' hi everything going good '
# for i in a:
#     print(i.replace('h', 'e', 2))

# swapping chars in string
# a = 'edwin'
# b = a[0]
# c = a[-1]
# d = a[1:-1]
# finalans = c+d+b
# print(finalans)


# a = input('enter your character ')
# b = input('enter character to replace ')
# c = input('enter the character to be replaced with ')
#
# str = a.replace( b, c)
#
# print('original word ', a)
# print('replaced word ', str)


# Append chars to string at end
# using concatenate
# a = input('enter your word ')
# b = input('enter the character you want to add ')
# c = a + b
# print(c)

# by using join method
# a = 'edwin'
# a = ''.join(a + 'n')
# print(a)
#
# b = 'thavamani'
# b = ' '.join(b[:3]+'hy'+b[3:])
# print(b)

# by using % operator
# a = "edwin"
# a = "edwin%s" %'n'
# print(a)

# # by using format operator
# a = "edwin"
# a = "edwin{}".format('n')
# print(a)

# find the lenght of the longest string in python
#
# a = ' hi everything is going good '
# b = a.split()
# print(b)
# print(type(b))
# max_length = 0
# for ele in b:
#     if len(ele) > max_length:
#         max_length = len(ele)
#         word = ele
#
#
# print(word)


# def edwin():
#     a = 20
#     b = 20
#     c = a * b
#     print(c)
# edwin()

#
# def prime():
#     num = int(input('enter your number '))
#     for i in range(2, num):
#         if num % i == 0:
#             print('it is not prime number')
#             break
#     else:
#         print('it is prime number')
# prime()
#
# list1 = [1, 2, 3, 3, 5]
# # list1.append(4)
# print(list1)
#
#
#
# list1.remove(2)
# print(list1)
#
# a = list1.copy()
# print(a)


# print(list1.count(3))

# a = [6, 7, 8]
# list1.extend(a)
# print(list1)
#
# list1.insert(2, 5)
# print(list1)
#
# x = lambda a: print(a * 10)
# print(x(5))


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.get('brand')
# print(x)
#
# x = car.copy()
# print(x)
# tuple
# x = car.items()
# print(x)
# only keys
# x = car.keys()
# print(x)

# car.pop('model')
# print(car)

#print(car)

# car.update({'color':'red'})
# print(car)

# only values
# # print(car.values())

# list2 = [1, 2, 5, 6]
# sum = 0
# for i in list2:
#     sum = sum + i
# print(sum)

# list2.reverse()
# print(g)

# list2.sort()
# list2.sort(reverse=True)
# print(list2)

#
# list1 = [1, 2, 5, 7]
# list2 = [1, 2, 5, 7]
#
# list3 = []
#
# for i in range(0, len(list1)):
#     list3.append(list1[i]+list2[i])
# print(list3)


# def square_num():
#     a = int(input('enter the number '))
#     b = int(input('enter the number till you want the square '))
#     for i in range(a, b+1):
#         print(i**2)
# square_num()


# def append_char():
#     a = 'edwin'
#     b = a[:3] + 'n' + a[3:]
#     print(b)
# append_char()

# def length_string():
#     a = input('enter your sentence ')
#     b = a.split()
#     max_length = 0
#     for i in b:
#         print(i)
#         if len(i) > max_length:
#             max_length = len(i)
#             c = i
#     print(c)
# length_string()


# nth index character from string
# def nth_index(str, n):
#     first_part = str[:n]
#     second = str[n+1:]
#     return first_part+second
# print(nth_index('edwin', 1))


# a = input('your string ')
# b = int(input('enter your index'))
# c = a[:b]
# print(c)
# d = a[b+1:]
# print(d)
# e = c + d
# print(e)

# def nth_number(a, b, g):
#     c = a[:b] + g
#     print(c)
#     d = a[b+1:]
#     print(d)
#     e = c + d
#     print(e)
# nth_number('edwin',1 , 'nnn')

# First last chars swapping

# a = input('your name   ')
# d = a[1:-1]
# b = a[:1]
# c = a[-1:]
# print(d)
# print(b)
# print(c)
# print('swapping both characters')
# print(c+d+b)


# Remove odd index values
# def odd_index(a):
#     result = ""
#     for i in range(len(a)):
#         print(i)
#         if i % 2 != 0:
#             result =result + a[i]
#     return result
# print(odd_index('edwin'))

# Count words in a string
#
# def count_words(a):
#     b = a.split()
#     print(b)
#     for i in range(len(b)):
#         count = i+1
#     print(count)
#     print(type(count))
#     print(len(a))
# count_words('edwin is very good boy')
#

# upper lower case of a string
# def upper_lower(a):
#     b = input("press 1 for uppercase or 2 for lowercase ")
#     if b == "upper":
#         print(a.upper())
#     elif b == "lower":
#         print(a.lower())
#     else:
#         print("entered case doesn't valid")
#
# upper_lower('edwin')

# Upper lower case of a string
# def upper_lower(a):
#     b = a.swapcase()
#     print(b)
# upper_lower('thAvAmani')
# upper_lower('eDwin')

# Sort unique words alphanumerically
#
# a = input('enter your name ')
# b = a.split()
# print(b)
# b.sort()
# print(b)

# create HTML from string


# #Insert string in middle of speical chars
#
#
# a = input('enter your string name ')
# b = input('enter special characters')
# c = (b + a + b)
#
# print(c)
#
# def insert_string(str, chars):
#     c = (str + chars +str)
#     print(c)
# insert_string('$','edwin')

# # 4 Copies of last 2 chars
# def copies(a):
#     b = a[-2:] + " "
#     c = b * 4
#     print(c)
#
# copies('edwin')
#
# str1= "hello"
# s = (str1[:-2]+" ")*2
# print(s)


# Length of first 3 chars

# def first_3(a):
#     b = a[0:3]
#     c = len(b)
#     print(c)
# first_3('ed')


# def multiple_4(a):
#     b = len(a)
#     if b % 4 == 0:
#         print(a[::-1])
#     else:
#         print(a)
# multiple_4('edwi')


# d = ""
# a = input('enter your statements')
# b = a.split()
# print(b)
# for i in b:
#     c = len(i)
#     if c % 4 == 0:
#         d+=i[::-1]+" "
#        # print(d)
#     else:
#         d+=i+" "
# print(d)
#
# x=" ".join (b)
# print(x)

# #program to sort a string lexicographically
# a = input('enter your name')
# b = sorted(a)
# print(b)


# program to remove a newline in Python

# a = 'Python Exercises\nedwin'
# print(a)
# print(a.replace('\n',' '))

# program to check whether a string starts with specified characters
# def check_string(a):
#     b = a[0:1]
#     print(b)
#     if b.isalnum():
#         print('there is no special character')
#     else:
#         print('it is special character')
#
# check_string('@Aedwin')

#display formatted text (width=50) as output

# import textwrap
# sample_text = '''
#   Python is a widely used high-level, general-purpose, interpreted,
#   dynamic programming language. Its design philosophy emphasizes
#   code readability, and its syntax allows programmers to express
#   concepts in fewer lines of code than possible in languages such
#   as C++ or Java.
#   '''
# print()
# print(textwrap.fill(sample_text, width=100))
# print()
#

# remove existing indentation from all of the lines in a given text
# import textwrap
# sample_text = '''
#     Python is a widely used high-level, general-purpose, interpreted,
#     dynamic programming language. Its design philosophy emphasizes
#     code readability, and its syntax allows programmers to express
#     concepts in fewer lines of code than possible in languages such
#     as C++ or Java.
#     '''
# text_without_Indentation = textwrap.dedent(sample_text)
# print()
# print(text_without_Indentation )
# print()
#
# import textwrap
#
# a = '''
# Python is a widely used high-level, general-purpose, interpreted, dynamic
# programming language. Its design philosophy emphasizes code readability,
# and its syntax allows programmers to express concepts in fewer lines of
# code than possible in languages such as C++ or Java.
#     '''
#
# text = textwrap.dedent(a).strip()
# print(text)


# to print the following floating numbers upto 2 decimal places

# to print the following floating numbers upto 2 decimal places
# a = float(input('enter the floating point numbers '))
# # print(round(a, 2))
# print("{:.2f}".format(a))
# print("%.2f"%a)
# print(f"{a:.2f}")



# copy, shallow copy , deep copy
import copy
# l1 = [1, 3, 5, 6,[1,2,3],[2,3,4]]
# l2 = l1
# print(l2)
# l1.append(7)
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))
# shallow copy

# l2 = copy.copy(l1)
# print(l2)
# print(l1)
#
# l2 = copy.deepcopy(l1)
# l1[1] = 4
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))
# l1[4][1] = 4
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))


# a = float(input('enter your float number'))
# b = input('enter your sign')
# print(b, (round(a, 2)))


# x = 3.1415926
# y = -12.9999
# print("\nOriginal Number: ", x)
# print("Formatted Number with sign: "+"{:+.2f}".format(x))
# print("Original Number: ", y)
# print("Formatted Number with sign: "+"{:+.2f}".format(y))
# print()
## print("{:.2f}".format(a))
# print("%.2f"%a)
# print(f"{a:.2f}")

# x = 3.256
# print("%.0f"%x)
# print(f"{x:.0f}")
# print("{:.0f}".format(x))
# # print(round(x))

#print the following integers with zeros on the left of specified width
# a = int(input('enter your number '))
# b = input('enter your string ')
# print("{:>3d}".format(a))

# a = "ravi   kiran der"
# # a.split()
# # b = "".join(a)
# # print(b)
# # print(b.strip())
# b = a.replace(" ","")
# print(b)
# # print(a.strip())


#to display a number with a comma separator
# a = input('enter your number')
# b = ",".join(a.split())
# print(b)
#
# for i in a:
#     print(i, end=",")

# to display a number in left, right and center aligned of width 10
# learn string formatting
# # to count occurrences of a substring in a string
# a = input('enter the string ')
# b = input('enter the string to find the occurances of sub string ')
# print(a.count(b))

# reverse a string
# a = input('enter a string to reverse it ')
# print(a[::-1])
# b = ''.join(reversed(a))
# print(b)
# str = " "
# for i in a:
#     str = i + str
# print(str)

# reverse a word in a string
# def reverse_word(a):
#     b = " ".join(reversed(a))
#     print(b)
# reverse_word('edwin is very good')
#
# string = "I am a python programmer"
# words = string.split()
# print(words)
# words = list(reversed(words))
# print(words)
# print(" ".join(words))
#

# a = input('enter your name ')
# b = a.split()
# print(b)
# c = ' '.join(reversed(b))
# print(c)

# a = input('enter your name ')
# b = a.index()
# print(b)

# print the index of the character in a string

# a = lambda x, b: x + b
# # print(a(20,30))
# # print(a(40,10))
#
#
# class edwin:
#     def __init__(self,name):
#         self.name = name
#
#     def amir(self,age):
#         self.age = age
#         print(self.name,self.age)
# obj = edwin('edwin')
# obj.amir( 25)
#
# class student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#
#     def display(self):
#         print('hi',self.name)
#         print('hi',self.age)
#
#     def marks_i(self):
#         if self.marks >= 600:
#             print('you got first grade')
#         else:
#             print('you are failed')
#
# s = student('edwin',25,50)
# s.display()
# s.marks_i()

# class Dog:
#     # Class Variable
#     animal = 'dog'
#
#     # The init method or constructor
#     def __init__(self, breed):
#         # Instance Variable
#         self.breed = breed
#
#     # Adds an instance variable
#     def setColor(self, color):
#         self.color = color
#
#     # Retrieves instance variable
#     def getColor(self):
#         return self.color
#
#
# # Driver Code
# Rodger = Dog("pug")
# Rodger.setColor("brown")
# print(Rodger.getColor())






# l1 = [1,2,3,[],4,[]]
# a = [x for x in l1 if x != []]
# print(a)

# a = 'edwinin1345'
#
# l1 = list(a)
# for i in l1:
#     m=l1.count(i)
#     if m<1:
#         print(i)
#     else:
#         print(i)
# l2 = ''.join(l1)
# print(l2)
#
#
# def __str__(a):
#     pass
#
#
# print(__str__(a))

# a = [1,2,8,7]
# b = []
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]<a[j]:
#             a[i],a[j] = a[j],a[i]
# print(a)



# Find the highest 3 values in a dictionary.

