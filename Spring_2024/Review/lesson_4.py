

# def ispalindrom(a):
#     # a = a.lower()
#     # array = a.split(' ')
#     # new_text = ''.join(array)
#     # print(new_text)
#     # if new_text == new_text[::-1]:
#     #     return True
#     # else:
#     #     return False
#     # text = [x.lower() for x in a if x.isalpha()]
#     # return text[:] == text[::-1]
#
# text = 'А роза упала на лапу Азора'

# print(ispalindrom(text))

# result = lambda x: x.startswith('W')
# print(result('World'))

# sq = lambda x,y: x**2 + y**2
# print(sq(3,4))
#
# test = lambda x: x % 19 == 0 or x % 13 == 0
# print(test(26))

# data = ['год', 'день', 'демь','hello123123123', 'месяц']
#
# sorted_data = sorted(data, key = lambda x: (len(x),x))
# print(*sorted_data)

# a = [1,2,3,4,5,6,7,8]
# test = list(filter(lambda x: x % 2 == 0, a))
# print(test)


# numbers = [0, 1, 2, 4, 6, -2, -3, -4]
# result1 = list(filter(lambda x: x == 0, numbers))
# result2 = sorted(list(filter(lambda x: x < 0, numbers)))
# result3 = sorted(list(filter(lambda x: x > 0 , numbers)))
# print(result2+ result1 + result3)

# a = '1 2 3 4 5'
# b = list(map(int, a.split(' ')))
# print(b)


# def square (x):
#     return x ** x
#
# a = [1,2,3,4,5]
# b = list(map(square,a))
# print(b)
# a = ['Hello', 'World', 'Hi']
# b = list(map(str.upper, a))
# print(b)


# days = ['One', 'Two', 'Three', 'Six', 'Seven', 'siest']
# days_s = sorted(list(filter(lambda x: len(x) == 5 and x.upper().startswith('S'), days)))
# print(days_s)

# numbers = [1,2,3, -456, 123]
# new_numbers = list(map(lambda x: x * 3, numbers))
# print(new_numbers)


def decorator_function(func):
    def wrapper(*args):
        print('Hello')
        result = func(*args)
        print(func.__name__)
        print(result)
        print('Goodbye')
    return wrapper


@decorator_function
def square(x):
    return x ** x

square(5)

