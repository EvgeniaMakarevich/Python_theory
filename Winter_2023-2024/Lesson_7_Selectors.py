# from collections import deque
#
# favorite_fish_deque = deque(["Sammy", "Jamie", "Mary"])
#
# # O(1) performance
# favorite_fish_deque.appendleft("Alice")
#
# print(favorite_fish_deque)

from collections import Counter
my_string = 'Hello world'
print(Counter(my_string))

from collections import namedtuple

colors = namedtuple('colors','r g b')
red = colors(r =255, g =204, b= 505)
print(red.b)

print(4//2)