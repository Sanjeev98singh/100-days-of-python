# int()

# print(int('10'))
# print(int('10.5'))
# ValueError: invalid literal for int() with base 10: '10.5'
# print(int(True))
# print(int(10.5))
# print(int(0B1111))
# print(int('0B1111'))
# ValueError: invalid literal for int() with base 10: '0B1111'
# print(int('sanjeev'))
# ValueError: invalid literal for int() with base 10: 'sanjeev'

# float()

# print(float(10))
# print(float(10+20j))
# TypeError: float() argument must be a string or a real number, not 'complex'
# print(float(True))
# print(float('10'))
# print(float(True))
# print(float('0B1111'))
# ValueError: could not convert string to float: '0B1111'

# print(float(0B1111))
# print(float('sanjeev'))
# ValueError: could not convert string to float: 'sanjeev'

#  complex()

# print(complex(10))
# print(complex(10.5))
# print(complex(True))
# print(complex(False))
# print(complex(True))
# print(complex('10'))
# print(complex('10.5'))
# print(complex(0B1111))
# print(complex('0B1111'))
# ValueError: complex() arg is a malformed string
# print(complex('sanjeev'))
# ValueError: complex() arg is a malformed string

#  complex(x,y)

# print(complex(10,20))
# print(complex(10.5,20.7))
# print(complex(True,False))
# print(complex('10','20'))
# TypeError: complex() can't take second arg if first is a string
# print(complex(10,'20'))
# TypeError: complex() second arg can't be a string
# print(complex('10',20))
# TypeError: complex() can't take second arg if first is a string
# print(complex(10,20.7))



