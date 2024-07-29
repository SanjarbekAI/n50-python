# def f1(f2):
#     f2()
#
#
# def f2():
#     print("Hello")
#
#
# f1(f2)
from datetime import datetime

# def my_decorator(func):
#     def wrapper():
#         print("Started")
#         func()
#         print("Ended")
#
#     return wrapper
#
#
# @my_decorator
# def greeting():
#     print("Hello")
#
#
# @my_decorator
# def greeting2():
#     print("Hello")

# def timer(func):
#     def wrapper():
#         start = datetime.now()
#         func()
#         end = datetime.now()
#         print(end - start)
#
#     return wrapper
#
#
# @timer
# def register():
#     name = input("Name: ")
#     age = input("Age: ")
#     print(name, age)
#
#
# register()
import random


# def my_decorator(func):
#     def wrapper():
#         result = func()
#
#         return result * -1
#
#     return wrapper
#
#
# @my_decorator
# def random_num():
#     return random.randint(1, 100)
#
#
# print(random_num())

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#
#         return result * -1
#
#     return wrapper
#
#
# @my_decorator
# def add(a, b, c, **kwargs):
#     print(kwargs)
#     return a + b + c
#
#
# print(add(1, 2, 3, d=3))


# class Person:
#     num = 1
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def birthday(self):
#         return datetime.now().year - self.age + self.num
#
#     @staticmethod
#     def summa(*args):
#         return sum(args)
#
#     @classmethod
#     def new_init(cls, name, year):
#         age = datetime.now().year - year
#         return cls(name, age)
#
#     @classmethod
#     def change_num(cls):
#         cls.num = 2
#
#
# p1 = Person('John', 22)
# print(p1.birthday)

# Person.change_num()
#
# p1 = Person('John', 22)
# p2 = Person('John', 22)
# print(p1.birthday())
# print(p2.birthday())
