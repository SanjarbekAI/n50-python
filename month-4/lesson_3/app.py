# from decimal import Decimal
#
# print(Decimal('0.1') + Decimal('0.2'))
# #
# from collections import namedtuple
# #
# p = namedtuple('person', ('name', 'age'))
# #
# #
# persons = (p("john", 22), p("john", 22))
# # for obj in persons:
# #     print(obj.name)


# from collections import namedtuple
#
# color = namedtuple('rgb', ['red', 'green', 'blue'])
# colors = (color(255, 255, 255), color(255, 255, 255), color(255, 255, 255))
#
# for color in colors:
#     print(color)


# from decimal import Decimal, DecimalException
# from collections import namedtuple
#
#
# def get_data():
#     expense = namedtuple('Expense', ('reason', 'price'))
#     try:
#         reason = input("Reason: ")
#         price = Decimal(input("Price: "))
#
#         return expense(reason=reason, price=price)
#     except DecimalException:
#         print("Invalid price !")
#         get_data()
#
#
# def show_expenses(expenses: list):
#     if expenses:
#         total = Decimal('0.0')
#         for exp in expenses:
#             print(f"{exp.reason} \t -> ${exp.price} ")
#             total += exp.price
#         print(f"\n\nTotal Expenses: {total}")
#     else:
#         print("You have no expenses")
#         get_expenses()
#
#
# def get_expenses():
#     expense = get_data()
#     expenses = []
#     while expense.reason != "calculate":
#         expenses.append(expense)
#         expense = get_data()
#
#     else:
#         show_expenses(expenses)
#
#
# if __name__ == "__main__":
#     get_expenses()