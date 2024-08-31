# age = 10
# print(+age) always 10
# print(++age) always 10
# print(+++age) always 10

# age = 10
# print(-age) always -10
# print(--age) always -10
# print(---age) always -10

# num1,num2 = 10,20
# num3 = 30 if num1 < num2 else 40
# print(num3)

# num1 = int(input('Enter First Number'))
# num2 = int(input('Enter Second Number'))

# min = num1 if num1 < num2 else num2

# print('printed minimum value: ',min)

# minimum of three numbers
# nested conditional operator


# num1 = int(input('Enter First Number: '))
# num2 = int(input('Enter Second Number: '))

# s1 = 'Both Numbers are equal'
# s2 = 'First Number is greater than second'
# s3 = 'First Number is less than second'

# results = s1 if num1==num2 else s2 if num1>num2 else s3
# print(results)

# print(max(1,2,3,4,5,6,7,8,9))
# print(min(1,2,3,4,5,6,7,8,9))

# special operartors


# num1 = 10
# num2 = 10

# print(num1 == num2)
# print(num1 is num2)
# print(num1 is not num2)
# print(id(num1),id(num2))

# s1 = 'sanjeev'
# s2 = 'ravi'

# print(s1 == s2)

# print(s1 is s2)
# print(s1 is not s2)

# print(id(s1),id(s2))


# l1 = [1,2,3,4,5,6,7,8]
# l2 = [1,2,3,4,5,6,7,8]

# print(l1 == l2)

# print(l1 is l2)
# print(l1 is not l2)

# print(id(l1),id(l2))


# membership operator

# s = 'hii how are you doing this and what about it?'

# print('h' in s)

# print('hi' not in s)

# print('and' in s)

# print('hello' in s)

# print('world' not in s)

# l1 = [1,2,3,4,5,6,7,8]

# print(2 in l1)

#module

# import sanjeev as sv

# print(sv.PI)
# print(sv.name)
# sv.add(10, 20) 
# sv.mult(10, 20)

# from sanjeev import PI,name 
# from sanjeev import *

# print(PI)
# print(name)
# add(10, 20) 
# mult(10, 20)

# from sanjeev import add as a

# print(PI)
# print(name)
# a(10, 20) 
# mult(10, 20)
# import math

# print(math.pi)

# print(math.sqrt(16))

# from math import *

# print(pi)

# print(sqrt(16))

# import math as m

# print(m.pi)

# print(m.sqrt(16))

# import math 
# print(dir(math))

# from math import *
# print('PI: ',pi)
# print('E: ',e)
# print(ceil(10.1))
# print(floor(10.1))

# area of circle
# r = int(input('Enter the radius'))
# print(pi*r*r)


# random module

# from random import randint
from random import *
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
