class Person:
    country = 'USA'

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def email(self):
        return f'{self.name}.{self.surname}@gmail.com'


    def hello(self):
        return print(f'Hello,{self.name}')

    @classmethod
    def new_country(cls, new_country):
        cls.country = new_country
        return new_country

    @staticmethod
    def is_adult(age):
        return age > 18


person_1 = Person('Jane', 'Johnson')
# print(person_1.name)

person_1.hello()


class Programmer(Person):
    def __init__(self,name,surname, language,job, salary):
        super().__init__(name,surname)
        self.language = language
        self.job = job
        self.__salary = salary

    def coding(self):
        return f'My programming language is {self.language}'

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary


coder_1 = Programmer('Mike', 'Clause', 'Python', 'QA', '1000')

# coder_1.set_salary('1200')
# print(coder_1.get_salary())
#
# # print(coder_1.coding())
# #
# # print(person_1.country)
# # print(person_1.__dict__)
#
#
#
# coder_1.new_country('Georgia')
# print(coder_1.country)


print(Person.is_adult(15))
print(coder_1.email)
coder_1.name = 'Bob'
print(coder_1.email)



