# class Base:
#     def method(self):
#         print("Method of base")
#
#
# class Parent1(Base):
#     def method(self):
#         print("method of parent1")
#
#
# class Parent2(Base):
#     def method(self):
#         print("method of parent2")
#
#
# class Child(Parent1, Parent2):
#     def method(self):
#         super().method()
#
#
# obj1 = Child()
# obj1.method()
#
# print(Child.__mro__)
