# nums = iter([1, 2, 3])
# print(nums.__next__())
# print(nums.__next__())
# print(nums.__next__())
#
import time

#
# for i in iter([1, 2]):
#     print(i)

range(10)


# class CustomRange:
#     def __init__(self, start=0, end=None, step=1):
#         if end is None:
#             end = start
#             start = 0
#
#         if step == 0:
#             raise ValueError("step can not be zero")
#
#         self.step = step
#         self.current = start
#         self.end = end
#         self.start = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.current <= self.end:
#             self.current += self.step
#             return self.current - self.step
#         raise StopIteration
#
#
# for i in CustomRange(1, 100, 3):
#     print(i)


# class OddNums:
#     def __init__(self, numbers):
#         self.numbers = numbers
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.numbers) - 1:
#             self.index += 1
#             if self.numbers[self.index] % 2 == 1:
#                 return self.numbers[self.index]
#         raise StopIteration
#
#
# nums = [1, 2, 5, 63, 2, 22, 43, 5, 2, 5, 6453, 3]
#
# odd_nums = OddNums(nums)
#
# for num in odd_nums:
#     print(num)

# def unlimited_nums():
#     i = 1
#     while True:
#         yield i
#         yield i + 1
#         yield i + 2
#         i += 1
#
#
# for num in unlimited_nums():
#     print(num)
#
# def read_line():
#     with open('large.txt', 'r') as file:
#         for line in file:
#             return line
#
#
# for i in read_line():
#     print(i)
#
#
# """
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# """
# def fibonacci(ending: int):
#     a, b = 0, 1
#     while a < ending:
#         yield a
#         a, b = a + b, a
#
#
# for n in fibonacci(100):
#     print(n)
