# # LIST
#
# lst = [10, 'Hello', None, True, 25, 26.5]
# # print(lst.index(25))
# # print(len(lst))
# # print(id(lst))
# # text = 'Bye'
# # lst.append(text)
# # print(lst)
# # print(id(lst))
# #
# # # lst[-1] = 100
# # # print(lst)
# #
# # # lst.reverse()
# # # print(lst)
# #
# lst2 = []
# for i in lst:
#     if isinstance(i, int):
#         lst2.append(i)
#
# print(lst2)
# print(sum(lst2)-1)
# print(min(lst2))
# print(max(lst2))

# Добавление только строковых данных из листа 1 в лист 2
# list1 = [1,2,3,'Hello',4]
# list2 = []
# for x in list1:
#     if isinstance(x,str):
#         list2.append(x)
# print(list2)

# lst = [1,2,3,4]
# lst.insert(3,'Hello2')
# print(lst)

# Создание нового листа из данных другого листа одной строкой
# lst2 = [1,2,3]
# lst3 = [x*x for x in lst2 if x % 2]
# print(lst3)

# Такое же создание нового листа из данных другого листа (более длинное)
# lst = [1, 2, 3, 4, 5, 6]
# lst2 = []
# for i in lst:
#     if i % 2 == 0:
#         lst2.append(i*i)
# print(lst2)
#
# lst3 = [x*x for x in lst if x % 2 == 0]
# print(lst3)

# print(len(lst))
# print(lst.index(True))


# lst1 = [1,2,3, 5 ,6 ]
# lst2 = [x + 1 for x in lst1 if x % 2 == 0]
# print (lst2)

# lst1 = [1,2,3,4]
# lst2 = []
# for x in lst1:
#       if x % 2 == 0:
#           lst2.append(x+1)
# print(lst2)

# TUPLE

# my_tuple = 1, 2, 3
# print(type(my_tuple))
#
# my_tuple2 = ('lemon', 'mango', 'cherry')
# print(type(my_tuple2))
#
# my_tuple3 = ('lenon', )
# print(type(my_tuple3))
# my_tuple[0] = 'orange'
#
# lst = list(my_tuple)
# lst[0] = 'orange'
# my_tuple = tuple(lst)
# print(my_tuple)

# def sum_it(*args):
#     return sum(args)
#
#
# print(sum_it(2,5,8,25))
# print(sum_it(2,5,8,25,2,5,8,25))


# def func(*args):
#   for item in args:
#     return item * item
# print(func(2, 5, 6, 10))


# def sum_it(*args):
#     return sum(args)
# print(sum_it(2,5,9))
#
# def square(*args):
#     for x in args:
#         return x * x
# print(square(1,2,3))

# Сортировка листов:

# lst1 = [2,3,4,1,6]
# print(sorted(lst1))

# lst = [1,2,3,7,6,8]
# lst.sort()
# print(lst)

# CЛОВАРИ:

# my_dict = {
#     'name' : 'Alex',
#     'last name' : 'Smith',
#     'age':12,
#     'dep':'DEV'
# }
#
# my_dict.pop('name')
# print(my_dict)
#
# my_dict['name'] = 'JANE'
# print(my_dict)

# print(my_dict)
# print(my_dict['last name'])
#
# # ПОМЕНЯТЬ ЗНАЧЕНИЕ КЛЮЧА
# my_dict['dep'] = 'IT'
# print(my_dict)

# print(my_dict.values())
# print(my_dict.keys())
# print(my_dict.items())
# print(len(my_dict))

# def x(**kwargs):
#     return kwargs
# print(x(name = 'Alice', surname = 'Komarova'))

# print(my_dict.get('name'))
# print(max(my_dict))
# print(type(my_dict))


# SETS

# my_set = set()
# print(my_set)

# my_list = [1,2,3,5,8,10,12,10]
# print(my_list)
# my_unique_list = list(set(my_list))
# print(my_unique_list)


# set1 = {1,2,3,'one', 'ten'}
# set2 = {1,2,3,'one', 'ten', 100, 525}
# set3 = {1,2,3}

# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set3.issuperset(set1))
# print(set1.difference(set3))

# set1.remove(1)
# print(set1)
#
# set2.add('Hello')
# print(set2)

# fs = frozenset({1,2,3})
# fs.remove(1)- нельзя удалить/добавить




# Вложенный лист

# lst = [5, [ 'a', 'b' ,'c'], 6]
# print(lst[1][1])
# print(lst[1][2])

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.setdefault('color','white')
# print(x)