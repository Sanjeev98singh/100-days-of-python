# s = {}
# print(type(s)) treated as dictionary

# s = set()
# print(type(s)) treated as SET
# s = {1,2,3,5}
# print(type(s)) treated as SET

# frozenset
#same like set but it is immutable in nature
# s = {1,2,3,5}
# fs = frozenset(s)
# print(type(fs))

# dict

# d = {1:'sanjeev', 2:'vicky', 3:'ujjwal'}
# print(type(d))
# print(d)

# d = {}
# # d[key] = value
# d[1] = 'sanjeev'
# d[2] = 'sanjeev'
# d[3] = 'yo'
# d[4] = 'sanjeev'
# d[5] = 'sanjeev'
# print(type(d))
# print(d)
# print(d[3])

# d = {1:'sanjeev', 2:'vicky', 3:'ujj', 'shvvh':2}
# print(d['shvvh'])
# print()
# key values we can make same if we compared to other key values
# a,b,c = 1,2,3   
# d = {a:'sanjeev', b:'vicky', c:'vic'}
# d[c] = 'dasgjdgdg'
# print(d)
# print(type(d))

# d = {1:'sanjeev', 1:'vicky', 1:'ujj'}  {1: 'ujj'}
# print(d)

# d = {1:['sanjeev', 'vicky', 'vic']}
# print(d)

# range(form-1)

# r = range(10)
# # print(r)  range(0, 10)
# for x in r:
#    print(x)

# print(type(r))

# form-2
# r = range(1,5)
# for x in r:
#     print(x)

# form-3

# r = range(1,11,2)
# # r = range(15,1,-2)

# for x in r:
#     print(x)

# r  = range(10,5)

# for x in r:
#     print(x) nothing

# r = range(0,101,5)

# for x in r:
#     print(x)

# or
# l = []

# for x in range(0,101,5):
#     print(x)

# or

# l = []
# for x in range(0,101,5):
#     l.append(x)

# print(l)

# r = range(10)
# # print(r[1])
# # print(r[-1])
# # print(r[2:4]) range(2, 4)
# r[1] = 7777 TypeError: 'range' object does not support item assignment
# print(r)

# bytes (0,255) same as range

# l = [1, 2, 3, 4, 5, 6, 256] ValueError: bytes must be in range(0, 256)
# l = [0, 1, 2, 3, 4, 5]
# b= bytes(l)
# print(b[0:2])

print(type(b))