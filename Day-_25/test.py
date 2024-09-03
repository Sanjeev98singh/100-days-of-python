# COMMAND LINE ARGUMENTS:

# command line arguments are passed to the script when it is run from the command line

from sys import argv

# print(type(argv)) <class 'list'>
# print('The number of command line arguments: ',len(argv))   #python test.py 10 20 30 ->  The number of command line arguments:  4
# print('The number of command line arguments: ',argv)       #The number of command line arguments:  ['test.py', '10', '20', '30']
# print(f'First argument {argv[0]}, second argument {argv[1]}, third argument {argv[2]}, fourth argument {argv[3]}')
# for x in argv:
#     print(f'{argv}')     # ['test.py', '10', '20', '30']
                         # ['test.py', '10', '20', '30']   
                       # ['test.py', '10', '20', '30']
                       # ['test.py', '10', '20', '30']

# for x in argv:
#     print(f'{x}') 
# test.py
# 1
# 2
# 3

# READ INT VALUES FROM THE KEYBOARD AS COMMAND LINE ARGUMENTS AND PRINT THE SUM

# x = argv[1:]
# print(x) #['1', '2', '3']

# x = argv[1:]
# sum = 0 
# for x1 in x:
#     n = int(x1)
#     sum += n
# print(f'The Sum: {sum}')    

# print(argv[1]) #Sanjeev Singh-> Sanjeev  
# print(argv[1]) #"Sanjeev Singh"/'Sanjeev Singh'-> Sanjeev Singh  

# print(int(argv[1])+int(argv[2])) #

# print(argv[100])  python test.py 1 2 3                 IndexError: list index out of range
