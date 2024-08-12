# f = 1.1011 allowed
# f = 0B1.1011 not allowed
# f = 0O1.1011 not allowed
# f = 0X1.1011 not allowed

# exponential form or scientific notation
# f = 1.2e3
# f = 1.2E3
# print(f)

# complex data type

# a + bj
# complex_data_type = 10 + 20j
# complex_data_type = 10.5 + 20.7j
# print(complex_data_type)
# print(type(complex_data_type))

# complex_data_type = 0B1111 + 20j
# print(complex_data_type)

# compile_complex_data_1 = 10 + 20j

# compile_complex_data_2 = 10.5 + 20.7j

# print(compile_complex_data_1 + compile_complex_data_2)
# print(compile_complex_data_1 - compile_complex_data_2)
# print(compile_complex_data_1 * compile_complex_data_2)
# print(compile_complex_data_1 / compile_complex_data_2)

# complex_data_type = 10 + 20.7j
# print(complex_data_type.real + complex_data_type.imag)

# bool data type 

# print(True + True)
# print(True + False)
# print(True * True)
# print(True + 20j)

# str data type

# string = 'sanjeev'
# string = "sanjeev"
# print(string + string)

# multi line  string literals

# string = '''sanjeev
#                     singh 
#                          bhadouria'''
# string = """sanjeev
#                     singh 
#                          bhadouria"""
# print(string)

# string = "i am sanjeev i know python and javascript 'despite of having knowledge of python and javascript' i am starting this repository to teach my juniors"
# string = 'i am sanjeev i know python and javascript "despite of having knowledge of python and javascript" i am starting this repository to teach my juniors'
# string = '''i am sanjeev "i know python and javascript" 'despite of having knowledge of python and javascript' i am starting this repository to teach my juniors'''
# string = '''i am sanjeev \"i know python and javascript\" \'despite of having knowledge of python and javascript\' i am starting this repository to teach my juniors'''


# print(string)

# string = 'sanjeev'
# print(string[6])
# print(string[-1])

# s = '................................................................................................................................'
# print(s[-1])
# print(s[len(s)-1])

# slice operator

# string = 'sanjeevsinghbhadouria'

# # print(string[0:8])
# # print(string[3:7])
# print(string[:7])
# # or
# print(string[0:7])
# print(string[3:])
# print(string[:]) full string from beginning of string to end of string
# print(string[0:500]) upto available characters it will print
# print(string[7:2]) empty string from beginning of string to end of string because we have not provided steps
# print(string.upper())
# print(string[0].upper() + string[1:])
# print(string[0:-1] + string[-1].upper())
# # or
# print(string[0:len(string) - 1] + string[-1].upper())
# # or
# print(string[:len(string) - 1] + string[-1].upper())
# print(string[0].upper() + string[1:-1] + string[-1].upper())
# # or
# print(string[0].upper() + string[1:len(string)-1] + string[-1].upper())
# string = 'sanjeev' + 10
# print(string)   error message

# string = 'sanjeev' + '10'
# string repetition operator
# string = 'sanjeev' * '10' error
# string = 'sanjeev' * 10 
# # or 
# string = 10 * 'sanjeev'
# print(string)

# print('sanjeev' * 'sanjeev')
print(4 * 'sanjeev' * 3)