# a = str(input("Введите строку:"))
# print(a.upper())
# a = str(input("Введите строку:"))
# def make_upper_case(s):
#      return s.upper()
# print(make_upper_case(a))


# def better_than_average(class_points, your_points):
#     num_of_class = len(class_points)
#     class_score = sum(class_points) / num_of_class
#         return class_score < your_points

# def position(alphabet):
#     return (ord(alphabet) - 96)

# hp = int(input('Введите очки: '))
# if hp > 0:
#     print ('True')
# else:
#     print ('False')

# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# year = int(input('Введите год:'))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Високосный')
#         else:
#             print ('Невисокосный')
#     else:
#         print ('Високосный')
# else:
#     print ('Невисокосный')

# year = int(input('Введите год:'))
# if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
#     print('Високосный')
# else:
#      print ('Невисокосный')

# text = str(input('Введите текст:'))
# number = int(input('Введите кол-во раз:'))
# i = 0
# while i < number:
#     print(text)
#     i += 1

# text = str(input('Введите текст:'))
# number = int(input('Введите кол-во раз:'))
# i = 0
# for i in range(number):
#     print(text)
#     i += 1

num1 = float(input('Введите первое число:'))
num2 = float(input('Ведите второе число: '))
operator = str(input('Введите оператор: '))
result = 0
if operator == '/':
    result = num1 / num2
elif operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '%':
    result = num1 % num2
elif operator == '**':
    result = num1 ** num2
else:
    result = 0
print(f'{num1} {operator} {num2} = {result}')

