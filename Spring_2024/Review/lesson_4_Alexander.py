# a = sum([1,2,3], start = 10)
# print(a)

# def start_my_sum(items, start=0):
#     count = start
#     for i in items:
#         count += i
#     return count
#
#
# a = start_my_sum([1,2,3], start = 20)
# print(a)

# n = 1

# def sumit():
#     global n
#     n += 1
#     return n
#
# sumit()
# print(n)

# print(callable(1)) >> False
# print(callable(sum)) >> True


# def mother():
#     a = 20
#
#     def son():
#         nonlocal a
#         a += 1
#
#     return son
#
# result = mother()
# result()

# def mother(z):
#     y = 20
#
#     def son(x):
#         print(x,y,z)
#
#     return son
#
# result = mother(5)
# result(1)

# def decorator(func):
#     def wrapper(*args):
#         print('Делаем что-то до')
#         result = func(*args)
#         print('Делаем что-то после')
#         return result
#     return wrapper
#
# @decorator
# def add(a,b):
#     return a + b
#
# print(add(3,4))

# new_add = decorator(add)
# print(new_add(5,8))


def func(a):
    return a > 0

numbers = [1,2,3,-4,-5]
result = filter(func, numbers)
result_1 = filter(lambda x: x > 0 , numbers)
print(*result)

print(*result_1)




