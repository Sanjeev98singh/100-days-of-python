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
a,b = 1,2
d = {a:'sanjeev', b:'vicky'}
print(d)
print(type(d))
