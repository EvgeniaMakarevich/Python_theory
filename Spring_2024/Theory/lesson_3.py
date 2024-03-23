# numbers = [1,2,3,4,5]
# numbers[0] = 10
#
# numbers_2 = [2,3,4,5]
#
# numbers.extend(numbers_2)
# # # numbers.sort()
# print(sorted(numbers))

# numbers.reverse()
# print(list(reversed(numbers)))


# print(numbers[:4])

# new_list = [x*2 for x in numbers if x % 2]
# print(new_list)

# print(numbers.count(2))


# string = 'Hello'
# new_string = string.replace('e', 'g')
# print(new_string)


# def func(*args):
#     for item in args:
#         yield item *10
#
# print(list(func(10,2,3)))

# num_1 = (1,2,3,4,)
# print(id(num_1))
#
# num_2 = list(num_1)
# print(id(num_2))



# my_dict = {
#     'name':'Alex',
#     'surname': 'Makarevich',
#     'age': 25,
#     'department': 'IT'
# }
# #
# # # print(my_dict)
# # print(my_dict['name'])
# my_dict['salary'] = '3000'
# # print(my_dict)
#
#
# # СЛОВАРЬ - МЕТОДЫ .KEYS(), .ITEMS(), .GET()
# # print(my_dict.keys())
# # print(my_dict.values())
# # print(my_dict.items())
# #
# # # (удаление ключа)
# # my_dict.pop('salary')
# # print(my_dict)
# #
# # print(my_dict.get('age'))
# # # ==
# # print(my_dict['age'])
#
# # for item in my_dict.items():
# #     print(*item)
#
#
# set1 = {1,2,3,'one','ten'}
# set_2 = {1,2,3,'one','ten', 100, 555}
# set_3 = {1,2,5}
#
# # print(set1.issubset(set_2))
# # print(set_2.issuperset(set1))
# #
# # print(set1.intersection(set_3))
# # print(set_2.difference(set1))
#
# set_3.add('Hello')
# print(set_3)
