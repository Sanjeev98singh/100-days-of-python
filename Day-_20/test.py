# class MyIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1

# my_iter = MyIterator(1, 5)
# for num in my_iter:
#     print(num)

# def my_generator(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1

# gen = my_generator(1, 5)
# for num in gen:
#     print(num)

