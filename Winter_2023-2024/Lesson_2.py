# number = 1
# if number == 5:
#     print('Equal to 5')
# elif number >5:
#     print('More than 5')
# else:
#     print('less than 5')

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
#         # break
#
# for i in range(2, 11, 2):
#     print(i)

# print(bool(0))

# i = ''
# if i:
#     print('True')
# else:
#     print('False')

# i = 5
# while i != 0:
#     print(i)
#     i -= 1


# for i in range(10, 0, -1):
#     print(i)



# def sum(x, y):
#     return x+y
#
# # print(sum(5,8))
#
# def power(n):
#     x= sum(5,8)
#     result = x ** n
#     return result
#
# print(power(2))

# age = int(input('Введите возраст:'))
# if age < 18:
#     print('Go home')
# else:
#     print('Welcome')


# x = 1
# while x < 10:
#     print(x)
#     x += 1


# x = 1
# while True:
#     print(x)
#     x += 1
#
# x1 = 10
# for i in range(10):
#     print(i)

# x1 = 'qwerty'
# for i in x1:
#     print(i)

# def suma(a,b):
#     c = a + b
#     return c
# x = suma(3, 5)
# print(x)

# a = suma(3,5)
# print(a)
#
# b = a * 10
# print(b)

# x = 10
# def change():
#     return x + 5
#
# print(change())

# for i in range(10):
#     if i == 5:
#         print(i)
#         break
#     print(i)


# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# a = float(input("Введите, сколько рекомендуется спать:"))
# b = float(input("Введите, максим время для сна:"))
# sleep = float(input("Введите, сколько спит Анна:"))
# if sleep in range(a, b+1):
# if a <= sleep <= b:
#     print('Это норма')
# if sleep > b:
#     print('Это пересып')
# if sleep < a:
#     print('Это недосып')
# if sleep < a:
#      print('Это недосып')
# elif a <= sleep <= b:
#     print('Это норма')
# else:
#      print('Это пересып')


# a = int(input())
# b = 1
# while b ** 2 <= a:
#     print(b ** 2)
#     b += 1


# word = str(input('Введите слово '))
# while len(word) >= 1:
#     print(word)
#     word = word[1:-1]

# a = int(input('Введите число a '))
# b = int(input('Введите число b '))
#
# for i in range(a,b+1):
#     if i % 3== 0  and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 ==0:
#         print('Buzz')
#     else:
#         print(i)

# word = str(input('Введите слово '))
# count = 0
# for i in word:
#     if i.lower() in 'gc':
#         count += 1
# lengh_word = len(word)
# print(f'{count/lengh_word*100:.3f} %')

# numbers =input()
# a, b, c, d = map(int, numbers.split())
# print(a % 7 == 0 and b % 7 == 0)

# a = sum([5, 8])
# print(a)


# print(max(2,3,5))
s = 'Hello, world'
b = 'abc'
d = 1
e = 2
# print(len(s))
#
# for index, x in enumerate(s):
#     if x == 'l':
#         print(index)
#         break
# print(s.replace('l','o'))
# print(s.upper())
# print(s > b)
# print(str(d))
# print(type(s))
# print(50 +'50')

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")