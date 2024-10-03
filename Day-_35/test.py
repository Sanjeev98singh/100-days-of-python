# a, b = [int(x) for x in input('enter the number buddy:').split()]
# print(a, b) 1 2

# a = [int(x) for x in input('enter the number buddy:').split()]
# print(a) [1,2]
# a, b = [int(x) for x in input('enter the number buddy:').split(' ')]
# print(a, b)

# number = eval(input('enter the number'))
# print(number)
# print(type(number))

# number = eval("1+2+3")
# print(number)
# print(type(number))

# number = eval(input('enter the number'))
# print(number)
# print(type(number))

# lis = eval(input('enter the number'))
# print(lis)
# print(type(lis))

from sys import argv
print('length of arguments: ',len(argv))
print('number of arguments: ',argv)
for x in argv:
    # print(x)
    print(argv)