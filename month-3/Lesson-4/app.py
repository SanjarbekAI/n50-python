class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, new_gender):
        self.__gender = new_gender


p1 = People("John", 20, 'male')
"""
2. Kitoblarni ijarasini boshqaradigan class yozish kerak, hamma kitoblarni ro'yxatini ko'rish projectted bo'lishi kerak

add_book(book_name)
get_book(book_name)
return_book(book_name)
show_books()
"""


# class Bank:
#     def __init__(self, owner, deposit):
#         self.owner = owner
#         self.__deposit = deposit
#
#     def add_money(self, amount):
#         if amount > 0:
#             self.__deposit += amount
#             return self.__deposit
#
#         else:
#             return "Wrong amount."
#
#     def subtract_money(self, amount):
#         if 0 < amount <= self.__deposit:
#             self.__deposit -= amount
#             return self.__deposit
#         else:
#             return "Wrong amount."
#
#     def show_deposit(self):
#         return self.__deposit
#
#
# obj1 = Bank("John", 100)
# obj2 = Bank("raj", 1000)
#
# obj1.add_money(100000)
# obj2.subtract_money(1000)
#
#
# print(obj1.show_deposit())
# print(obj2.show_deposit())

class Lib:
    def __init__(self):
        self.__books = []
