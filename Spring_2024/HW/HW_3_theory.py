# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
#
# print(my_list[2][0],my_list[2][1], my_list[2][2] )


# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

# list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
# list_2 = [x for x in list_1 if type(x) == int]
# print(sum(list_2))

# print(sum(filter(lambda x: type(x) == int, list_1)))




# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

# list_1 = ['cat', 'dog', 'horse', 'cow']
# tuple_1 = tuple(list_1)
# print(tuple_1)


# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# fam_1 = list(input('Enter family_1: '))
# fam_2 = list(input('Enter family_2: '))
#
# def count_number(family_1, family_2):
#     if len(family_1) > len(family_2):
#         print('Family_1 is bigger')
#     elif len(family_2) > len(family_1):
#         print('Family_2 is bigger')
#
#     else:
#         print('Equal')
#
#
# count_number(fam_1, fam_2)


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение


my_dict = {
    'title': 'Friends',
    'director': 'Mark',
    'year': '2000',
    'budget': '123123 usd',
    'main_actor': 'Jeniffer Aniston',
    'slogan': "I'll be there for you"
}
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# for key, value in my_dict.items():
#     print(f'{key}:{value}')


# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))


# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
#
# list_1 = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(list_1))

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#
# print(set2.intersection(set1))
# print(set2.difference(set1))
# print(set1.issubset(set2))

# weight = int(input())
# print(weight)
#
# flag = True
# flag_1 = not flag
# print(flag_1)

testing = [1,2,3]
print(len(testing))