import time

import pytest
# def sum (a,b,c=5)

#     return a+ b+ c

# print(sum(3,4))
# print(sum(2,4,c = 10))

# name = 'Alice'
# def outer_function():
#     # name = 'Alex'
#     def inner_function():
#         # name = 'Albert'
#         return name
#     return inner_function
#
# enclosure = outer_function()
# result = enclosure()
#
# print(result)

# def decorator_function(func):
#     def return_time(*args):
#         print(func.__name__)
#         time_before = time.time()
#         print(time_before)
#         print(func(*args))
#         time_after = time.time()
#         print(time_after)
#         general_time = time_after - time_before
#         print(general_time)
#     return return_time
#
# @decorator_function
# def sum_it(a, b):
#     return a * b
#
# sum_it(123345434, 45)

import math

# arr = [1,5,6,7,25]
# result = math.prod(arr)
# print(result)

# import datetime
#
# birth_year = 1985
# current_date = datetime.date.today()
# current_age = current_date.year - birth_year
# print(current_age)


# lamda functions

# res = lambda x,y: x * y
# print(res(2,3))

# l = [1,5,8,12,15]
# #
# # print(list(filter(lambda x: x % 2 == 0, l)))
#
# # my_list = ['Hi', 'my_name_a', 'ananas', 'Hello', 'allo', 39, 40]
# #
# # print(list(filter(lambda x: isinstance(x, str) and 'a' in x,  my_list)))
#
# from functools import reduce
#
# print(reduce(lambda x,y: x + y, l))