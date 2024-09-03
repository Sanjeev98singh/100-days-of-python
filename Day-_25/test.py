# COMMAND LINE ARGUMENTS:

# command line arguments are passed to the script when it is run from the command line

from sys import argv

# print(type(argv)) <class 'list'>
print('The number of command line arguments: ',len(argv))   #python test.py 10 20 30 ->  The number of command line arguments:  4
print('The number of command line arguments: ',argv)       #The number of command line arguments:  ['test.py', '10', '20', '30']
# print(f'First argument {argv[0]}, second argument {argv[1]}, third argument {argv[2]}, fourth argument {argv[3]}')