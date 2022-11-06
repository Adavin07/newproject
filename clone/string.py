a = "eDwin is very good"

# print(a.capitalize())
# print(a.casefold())
# print(a.upper())
# print(a.lower())
# print(a.isdigit())
# print(a.endswith("i"))
# print(a.center(30))
# print(a.count("is"))
# print(a.encode())
# print(a.expandtabs(20))
# print(a.find("b"))
# print(a.index("e", 4, 11))
# print(a.isalnum())
# print(a.isalpha())
# print(a.isdigit())
# print(a.isidentifier())
# print(a.split())
# print(a.swapcase())
# print(a.title())
#
#
# # write a program to calculate the length of a string
#
# a = "edwin"
# # print(len(a))
#
# a = "google.com"
# print(a.count())


# # remove special character from string
# x =10
#
# print(x)

# a = 20
# b = 20
# print(a==b)

# reverse words in a string
# a = input('enter the name ')
# b = a.split()
# print(b)
# c = ' '.join(reversed(b))
# print(c)

# strip a set of characters from a string
# a = input(' enter the name ')
# b = input(' enter the character to be removed from a ')
# c = " "
# for i in a:
#     if i not in b:
#         c = c + i
# print(c)

# count repeated characters from a string
# b = input('enter the sting  ')
# a = input('enter character to count repeated character ')
# count1 = 0
# for i in b:
#     if i == a:
#         count1 += 1
# print(count1)




# print the index of the character in a string


# a = input('enter the string to find the index  ')
# b = input('the character to find the index')
# c = a.index(b,2)
# print(c)

# a = input('enter the string to find the index ')
# c = input('enter the string to find the index of a ')
# b = len(a)
# for i in range(b):
#
#
#
# a = input('enter the string to find the index ')
# b = input('enter the character')
# c = a.count(b)
# print(c)
#
# a = input('enter the string to find the ')
# b = input('enter the string the find the index')
# c = 0
# for i in a:
#     if i == b:
#         c+=1
# print(c)

#
# a = input('enter the string to reverse')
# # b = ' '.join(reversed(a))
# print(b)

# b = a[::-1]
# print(b)


# b = a.split()
# d = " "
# for i in b:
#     c = i[::-1]
#     d = d +" "+ c
# print(d)

# a = input('print the index of the character ')
# b = input('input the character to find the index ')
# c = a.index(b)
# print(c)
# # for i in range(len(a)):
# #     if i == len(b):
# #         print(i)

# check if a string contains all letters of the alphabet
# a = input('enter string to check contains all ')

# convert a string in a list
#
# a = input('convert a string in a list')
# b = list(a)
# print(b)

# a = input('lowercase first n characters')
# for i in a:
#     if i.islower():
#         b = ''.join(list(i))
#         print(b)
#
# a = input('enter lower case to find first character or not')
# for i in a:
#     if i.islower():
#         print(i)
#         break
#
# a = input('enter the string to get vowels out')
# b = ['a','e','i','o','u']
# c = ""
# count = 0
# for i in a:
#     if i not in b:
#         c +=i
# print(c)


# a = "edwin,edwin,edwin,rajavelu"
# b = a.split(',')
# print(b)
# #
# a = input('find the first non repeating character in a string')
#
# for i in a:
#     if a.count(i) < 2:
#         print(a.index(i),i)

#
# a = 'laptop'
# b = dict(a)
# print(b)
#
# a = input('enter the string')

#
# b = (' edwin is very good very')
# c = b.split()
# for i in c:
#     if c.count(i) < 2:
#         print(i,end=" ")


# # find the second most repeated word in a given string
# a = ('edwin is very good very good is is')
# b = a.split()
# c = []
# for i in b:
#     if b.count(i) >= 2:
#         c.append(i)
#         print(i,end=" ")
# print(c)
# print(max(c))


# a = 'edw in'
# b = a.replace(' ','')
# print(b)


# capitalize first and last letters of each word of a given string
#
# a = 'edwin is very good'
# b = a.split()
# c = []
# for i in b:
#     x = i[0].upper()+i[1:-1]+i[-1].upper()
#     c.append(x)
# print(c)


# remove duplicate characters of a given string
# a = 'edwinin1345'
# count = 0
# for i in a:
#     if i.isnumeric():
#         print(i)
#         count = count + int(i)
# print(count)


# c = '1908.020.05.008'
# d = c.split('.')
# print(d)
# for i in range(len(d)):
#     if i[0] == 0:

# a = ' python'
# b = reversed(a)
# print(b)
#
a = ' rajavelu is good boy'
# b = a.split()
# print(b)
# for i in b:
#     print(i[::-1],end=" ")

# b = a.split()
# c = ''
# for i in b:
#     c = i +'  '+ c
# print(b)
# print(c)

a = [[1,2],[2,4]]
l1 = []
# l1.append(a[0][0] + a[1][0])
# l1.append(a[0][1] + a[1][1])
# print(l1)

# a = {'1':{'1':2,'2':'edwin'},'2':{'4':'yash','5':7}}
# print(a['1'])
#
# a = [[1,2],[2,4]]
# b = [[1,2],[2,4]]
# l1 = []
# for i, j in zip(a, b):
#     a = i[0] + j[0]
#     b = i[1] + j[1]
#     l1.append([a,b])
# print(l1)
# l1 = []
# count1 = 0
# count2 = 0
# for i in a:
#     count1 += i[0]
#     count2 += i[1]
# l1.append(count1)
# l1.append(count2)
# print(l1)
# l1 = [1,2,3,4]
# l2 = [1,2,3,4]
# l3 = []
# for i,j in zip(l1, l2):
#     l3.append(i+j)
# print(l3)
#
# a = [1,2,[3,4]]
# b = [1,2,[3,4]]
# l1 = []
# for i,j in zip(a,b):
#     if isinstance(i, int):
#         x = i + j
#         l1.append(x)
#     else:
#         x = i[0] + j[0]
#         y = i[1] + j[1]
#         l1.append([x,y])
#
# print(l1)

# l = [3, 6, 9]
#
#
# b = []
# for i in l:
#     b+=int(i)
#
# print(b)







