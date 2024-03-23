class Phone:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__owner = None

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        if owner == None:
           print('There\'s no owner')
        else:
            self.__owner = owner



iphone_1 = Phone('iPhone', '2020')

print(iphone_1.model)
# print(iphone_1._owner)
iphone_1.set_owner('Jane')
print(iphone_1.get_owner())

