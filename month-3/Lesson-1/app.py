# """
# try, except
#
# Exceptions:
# - SyntaxError
# - ZeroDivisionError
# - IndexError
# - KeyError
# - ValueError
# - TypeError
# - FileNotFoundError
# - ImportError
# - RecursionError
# - NameError
#
# """
#
# # try:
# #     age = int(input("Enter your age: "))
# #     print(age)
# # except Exception as exc:
# #     print(f"Invalid input {exc}")
#
#
# # def divide():
# #     try:
# #         num1 = int(input("Enter a number: "))
# #         num2 = int(input("Enter a number: "))
# #         print(num1 / num2)
# #     except ZeroDivisionError:
# #         print("You can't divide by 0")
# #         divide()
# #     except ValueError:
# #         print("Invalid input, enter a number")
# #         divide()
# #
# #
# #
# # divide()
#
# # Ama n a p l a nacan a l P a n ama
# # try:
# #     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #     print(nums[-100])
# # except BaseException:
# #     print("IndexError")
#
# # print(2 / 'ss')
#
# # try:
# #     import aka
# # except ImportError:
# #     print("no ")
#
#
# # def say_hello():
# #     print("Hello World!")
# #     say_hello()
# #
# #
# # say_hello()
#
# # names = {
# #     'ali': 12
# # }
# #
# # print(names['vali'])
#
# products = {
#     'apple': 5000,
#     'bread': 3000,
#     'water': 2500,
#     'chocolate': 20000
# }
#
#
# def calculate_price():
#     counter = 1
#     for product in products.keys():
#         print(f"{counter}. {product}")
#         counter += 1
#
#     try:
#         name = input("Enter product name: ")
#         quantity = int(input("Enter quantity: "))
#
#         result = f"{name} ({products[name]}) x{quantity} = {products[name] * quantity}"
#         print(result)
#     except KeyError:
#         print("Invalid product name")
#         calculate_price()
#     except ValueError:
#         print("Invalid quantity")
#         calculate_price()
#
#
# calculate_price()


def isPalindrome(s: str) -> bool:
    if s == s[::-1]:
        return True

    new_text = ""
    for char in s:
        if char.isalpha():
            new_text += char.upper()
    print(new_text)
    return new_text == new_text[::-1]


print(isPalindrome("0P"))
