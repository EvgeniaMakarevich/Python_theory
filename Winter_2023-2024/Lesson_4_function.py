# min_item = min(20,15,77,100)
# print(min_item)

# def person(age,first_name, last_name='Makarevich'):
#     return f'Hello, my name is {first_name} {last_name}. I am {age} years old.'
# # print(person(23,'Jane','Makarevich'))
# print(person(first_name="Jane", age = 23))

# def pattern(length, char1 ='', char_2='*'):
#      return (char1 + char_2) * length + char1
# print(pattern(9, char1 = '/'))

# def decorator_function(func):
#      def wrapper():
#           print('Wrapper function')
#           print(f'Wrapped function:{func.__name__}')
#           print('Wrapped function in process')
#           print(func())
#           print('Exiting wrapper')
#      return wrapper

# result = lambda n: n *n
# print(result(5))


# list_1 = ['Hi', "ananas", 2, None, 75, 'pizza', 36, 100]
# def filter_and_sum(lst):
#      new_l = []
#      for x in lst:
#           if isinstance(x,int):
#               new_l.append(x)
#      return sum(new_l)
# print(filter_and_sum(list_1))

# new_l = (filter(lambda x: isinstance(x,str),list_1))
# print(list(filter(lambda i: 'a' in i, new_l)))

# Декораторы

# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
# user = User('simple_user','user')
# admin = User('root', 'admin')
# current_user = admin
#
# def do_admin_work():
#     if current_user.role != 'admin':
#         raise Exception('Доступ запрещен!')
#     return "Делаем что-то доступное админу"
#
# print(do_admin_work())

# Алгоритм Евклида
# import time
# def get_nod(a,b):
#     # while a != b:
#     #     if a > b:
#     #         a -= b
#     #     else:
#     #         b -= a
#     # return a
#     if a < b:
#         a,b = b,a
#     while b != 0:
#         a,b = b, a % b
#     return a

# def test_nod(func):
#     a = 28
#     b = 35
#     res = func(a,b)
#     if res == 7:
#         print('test_1-ok')
#     else:
#         print('test_1-failed')
#
#     a = 100
#     b = 1
#     res = func(a,b)
#     if res == 1:
#         print('test_2-ok')
#     else:
#         print('test_2-failed')
#
#     a = 2
#     b = 100000000
#     st = time.time()
#     res = func(a,b)
#     et = time.time()
#     dt = et - st
#     if res == 2 and dt < 1:
#         print('test_3-ok')
#     else:
#         print('test_3-failed')


# res = get_nod(18,24)
# print(res)

# test_nod(get_nod)

# Область видимости
#  global x использовать глобальную переменную
# nonlocal x -сделать переменную x не только конкретной локали, но и локали выше

# Замыкание

# def say_name(name):
#     def say_goodbye():
#         print('Dont say me goodbye, '+ name + '!')
#     return say_goodbye
#
# f = say_name('Sergey')
# f()

# def counter(start=0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#     return step
#
#
# c1 = counter(10)
# c2 = counter()
#
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())


# def strip_string(strip_chars=' '):
#     def do_strip(string):
#         return string.strip(strip_chars)
#     return do_strip
#
# strip1 = strip_string()
# strip2 = strip_string('?!/.')
#
#
# print(strip1('Hellow python!..'))
# print(strip2('Hellow python!..'))


#Декораторы

# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Что-то делаем до')
#         res = func(*args, **kwargs)
#         print('Что-то делаем после')
#         return res
#     return wrapper
#
# @func_decorator
# def some_func(title, tag):
#     print(f'title = {title}, tag = {tag}')
#     return f'<{tag}>{title}</{tag}'
#
#
#
# # f = func_decorator(some_func)
# # f()
# # some_func = func_decorator(some_func)
# res = some_func('Python','h1')
# print(res)

# from functools import wraps
# import math
#
#
# def df_decorator(dx = 0.01):
#    def func_decorator(func):
#         @wraps(func)
#         def wrapper(x, *args, **kwargs):
#             res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#             return res
#         return wrapper
#    return func_decorator
#
# @df_decorator(dx = 23)
# def sin_df(x):
#     return math.sin(x)
#
#
# df = sin_df(math.pi/3)
# print(df)
#
# print(sin_df.__name__)



# Лямбда выражения = анонимные функции
# 1 пример
# def rectangle_area(a,b):
#     return a * b
#
#
# print(rectangle_area(17,14))

# =
# print((lambda a, b: a *b)(17,14))



# 2 пример
# def maximum(a,b):
#     if a > b:
#         return a
#     else:
#         return b
#
# print(maximum(7,5))


# print((lambda a, b: a if a > b else b)(25,14))


# print((lambda a: a * 4)(4))
# print((lambda a,b,c : (a+b+c)/3)(4,5,7))


# list_1 = ['Hi','ananas', 2, None, 75, 'pizza', 36, 100]
# def filter_and_sum(lst):
#     new_l = []
#     for x in lst:
#         if isinstance(x,int):
#                new_l.append(x)
#     return sum(new_l)
#
# print(filter_and_sum(list_1))


# FILTER -указываем условие до последовательности, если true-добавляет значения в новый отфильтрованный список

# a = [1,2,3,4,5,6,7,8,9]
# b = filter(lambda x: x % 2 == 0, a)
# lst = list(b)
# print(lst)

# new_l = sum(filter(lambda x: isinstance(x,int),list_1))
# print(new_l)



# def is_prost(x):
#     d = x - 1
#     if d < 0:
#         return False
#
#     while d > 1:
#         if x % d == 0:
#             return False
#         d -=1
#
#     return True
#
# a = [1,2,3,4,5,6,7,8,9]
#
# b = filter(is_prost, a)
# new_lst = list(b)
#
# print(new_lst)


# b_1 = filter(lambda x: x % 2 != 0, b)
# print(list(b_1))
# lst = ('Москва', 'Рязань1', "Смоленск", 'Тверь2', 'Томск')
#
# b_2 = filter (str.isalpha,lst)
# new_lst_2 = list(b)
# print(new_lst)

# list1 = ["Hi", 'ananas', 123, 'pizza', 34]
# b = list(filter(lambda x: isinstance(x,str) and 'a' in x,list1))
# print(b)


# REDUCE-применяем свойство ко всем числам-получаем одно значение(сall back функция)
# from functools import reduce
#
# result = reduce(lambda x,y: x*y, [1,5,8,11,13])
# print(result)

# MAP -перебор

# result = map(lambda x: x**2,[1,5,8,11,13])
# print(list(result))

# МОДУЛИ

# from math import prod
# import math as m
# from math import *
#
# l = [1,2,5,7]
# print(prod(l))


# from my_module import sum_it
#
# result = sum_it(5,9)
# print(result)

# def tests():
#     assert sum_it(5,8) == 13, f'Wrong number, actual result is {sum_it(5,8)}'
#     assert sum_it(10, 15) == 23, f'Wrong number, actual result is {sum_it(10, 15)}'
# tests()


# import datetime
#
# birth_year = 1984
# current_date = datetime.date.today()
# print(current_date)
#
# current_age = current_date.year - birth_year
# print(current_age)


# Домашнее задание
from math import *
4.1
# def square(x):
#     perim_square = x * 4
#     square_square = x ** 2
#     d = x * sqrt(2)
#     # lst=[]
#     # lst.append(perim_square)
#     # lst.append(square_square)
#     # lst.append(d)
#     # lst = tuple(lst)
#     return (perim_square,square_square, d)
#
# print(square(9))

4.2

# def test2(**kwargs):
#     for x, y in kwargs.items():
#         print(f'{x}:{y}')
#
# print(test2(name='John', surname='Ayr'))

4.3
# my_list = [20, -3, 15, 2, -1, -21]
#
# lst_new = list(filter(lambda x: x > 0, my_list))
# # print(lst_new)


4.4
# from functools import reduce
# lst_mult = reduce(lambda x,y: x * y,lst_new)
# print(lst_mult)


4.5

import time
#
# def time_count(func):
#     def wrapper(x, y):
#         start_time = time.time()
#         result = func(x, y)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Function '{func.__name__}' took {execution_time} to run.")
#         return result
#     return wrapper
#
# @time_count
# def example(x, y):
#     return x * y
#
# result = example(3, 4)



# def count_time(func):
#     def wrapper(x, y):
#         start_time = time.time()
#         func(x, y)
#         end_time = time.time()
#         exec_time = end_time - start_time
#         return print(f'Time for executing "{func.__name__}" is {exec_time}')
#     return wrapper
#
# @count_time
# def example(x,y):
#     return x*y
#
# example(100000000,120)


4.6
#
# from my_calc import sum
#
# print(sum(10,2))
#
# import my_calc
#
# print(my_calc.square(10,15))
#
# from my_calc import *
#
# print(minus(10,5))
#
# import my_calc as mc
#
# print(mc.mult(90,2))

# n1,n2,n3 = int(input()),int(input()),int(input())
# lst = [n1,n2,n3]
# pos = list(filter(lambda x: x > 0, lst))
# if sum(pos) > 0:
#     print(sum(pos))
# else:
#     print(0)


# b = list(map(int, ['1','2','3','4']))
# # print(next(b))
# # print(next(b))
# print(b)

# s = list(map(int, input().split()))
# print(s)


# def f(a,b):
#     return a * b

# d = map(lambda x: x+ 15,(2,4,5))
# print(list(d))

# from functools import reduce
#
# a = reduce(lambda a,b: a* b,(50,89,12,100))
# print(a)

# a = [1,2,3,10,5,6]
# b = 'abcdef'
#
# result = zip(a,b)
# print(list(result))


# SORT и SORTED

# a.sort()
# print(a)
# print(sorted(a)) -выдает список


# СЛОВАРИ

# dct = {1:'q', 2:'w'}
# for x in dct:
    # print(dct[x]) =получим value

# for x in dct.values():
#     print(x)
#
#
# for x,y in dct.items():
#     print(x,y)

# a = dct[1]
# print(a)

# a = dct.get(1)
# print(a)

# b = dct.setdefault(10,'qw')
# print(b)


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('before')
#         func(*args, **kwargs)
#         print('after')
#     return wrapper
#
# @decorator
# def run(a,b):
#     c = a + b
#     print(c)
#
# run(1,2)

# def factorial(n):
#     if n < 0 :
#         return None
#
#     result = 1
#     for i in range(1, n + 1)
#         result *= i
#     return result

#Рекурсия (замыкание)-функция вызывает саму себя


# def is_palindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrom(s[1:-1])
#
# print(is_palindrom('шалаш'))

# def generate_fizz_buzz_list(n):
#     lst = []
#     for x in range(1,n+1):
#         if x % 3 ==0 and x % 5 == 0:
#                lst.append('FizzBuzz')
#         elif x % 3 == 0:
#                 lst.append('Fizz')
#         elif x % 5 == 0:
#                 lst.append('Buzz')
#         else:
#                  lst.append(int(x))
#     return lst
#
# print(generate_fizz_buzz_list(10))


# start_with = lambda x: True if x[0].isupper() else False
# print(start_with('Hello'))
# numbers = [1,2,3,4,5,6,7,8]
# odds = list(filter(lambda x: x % 2 == 0, numbers))
# print(odds)

# def ispalindrom(string):
#     return string == string[::-1]
#
# print(ispalindrom('шалаш'))




list_1 = [1,2,3,[1,2,3],4,5]
list_2 = list_1[3]
print(*list_2, sep='\n', end='!')