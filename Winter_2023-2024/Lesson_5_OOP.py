# class Person:
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self._age = age
#
#     def hello(self):
#         return f'Hello, my name is {self.name} {self.surname}'
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#
# person_1 = Person('Alex', 'Baker', 30)
#
#
# person_1.set_name('Sasha')
# print(person_1.hello())




# print(person_1._age)

# print(person_1.__dict__) >> распечатать атрибуты







# print(person_1.name)
# print(person_1.surname)

# print(person_1.hello())
#
# person_1.name = 'Alexander'
# print(person_1.name)

# class Tester(Person):
#
#     def __init__(self,name,surname, framework):
#         super().__init__(name, surname)
#         self.framework = framework
#
#     def test(self):
#         return 'I love testing'
#
#
# tester_1 = Tester('Jane','Makarevich', 'pytest')

# print(tester_1.framework)
# print(tester_1.test())


#  PROPERTY

# class Person:
#     def __init__(self,age):
#         self.age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         if 0 <= age < 120:
#             self._age = age
#         else:
#             self._age = 0
#
#
# h = Person(30)
# h.age = 150
# print(h.age)



