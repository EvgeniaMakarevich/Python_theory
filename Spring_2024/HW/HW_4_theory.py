# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.



# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def func(**kwargs):
#     result = ''
#     for x, y in kwargs.items():
#         result += f'{x} : {y}\n'
#     return result
#
# print(func(name='John', last_name='Smith', age = 96, job_title= 'QA'))

# 	age: 35
# 	position: web developer))

#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x >=0, my_list)))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
from functools import reduce
# print(reduce(lambda x,y : x * y, my_list))
# print(reduce(lambda x,y : x * y, [x for x in my_list if x >0]))

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

# import time
# def decorator_function(func):
#     def return_time(*args):
#         print(func.__name__)
#         time_before = time.perf_counter()
#         print(f'time_before = {time_before}')
#         print(f'функция выполняется : {func(*args)}')
#         time_after = time.perf_counter()
#         print(f'time_after = {time_after}')
#         general_time = time_after - time_before
#         print(f'general_time = {general_time}')
#     return return_time
#
# @decorator_function
# def sum_it(a, b):
#     return a * b

sum_it(123345434, 45)

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.