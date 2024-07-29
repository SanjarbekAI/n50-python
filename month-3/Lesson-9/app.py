# import hashlib
# from datetime import datetime
# from typing import Union
#
# from file_managing import student_manager, product_manager, order_manager
#
# admin_id = "00"
# admin_password = "00"
#
#
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = float(price)
#         self.quantity = quantity
#
#
# class Student:
#     def __init__(self, full_name, student_id, student_password):
#         self.full_name = full_name
#         self.student_id = student_id
#         self.student_password = student_password
#         self.is_login = False
#         self.coin = 100
#
#     def check_password(self, confirm_password):
#         return confirm_password == self.student_password
#
#     @staticmethod
#     def hash_password(student_password):
#         return hashlib.sha256(student_password.encode()).hexdigest()
#
#
# def register():
#     full_name = input("Enter full name: ")
#     student_id = input("Enter student id: ")
#     student_password = input("Enter your password: ")
#     confirm_password = input("Enter your confirm password: ")
#
#     student = Student(full_name, student_id, student_password)
#     if not student.check_password(confirm_password):
#         print("Passwords do not match")
#         return register()
#
#     student.student_password = Student.hash_password(student_password)
#     student_manager.add_data(data=student.__dict__)
#     return show_auth_menu()
#
#
# def login():
#     student_id = input("Enter student id: ")
#     student_password = input("Enter your password: ")
#     if student_id == admin_id and student_password == admin_password:
#         return show_admin_menu()
#     hashed_password = Student.hash_password(student_password)
#
#     all_users = student_manager.read()
#
#     index = 0
#     while index < len(all_users):
#         if all_users[index]['student_id'] == student_id and all_users[index]['student_password'] == hashed_password:
#             all_users[index]['is_login'] = True
#             student_manager.write(all_users)
#             return show_menu()
#         index += 1
#     student_manager.write(all_users)
#     print("User not found, or password is incorrect")
#     return show_auth_menu()
#
#
# def logout_all():
#     all_users = student_manager.read()
#     index = 0
#     while index < len(all_users):
#         all_users[index]['is_login'] = False
#         index += 1
#     student_manager.write(all_users)
#     return show_auth_menu()
#
#
# def add_product():
#     name = input("Enter product name: ")
#     price = int(input("Enter product price in coin: "))
#     quantity = int(input("enter product quantity: "))
#     product = Product(name, price, quantity)
#
#     product_manager.add_data(product.__dict__)
#     print('Product added successfully!')
#     return show_admin_menu()
#
#
# def delete_product():
#     name = input("Enter product name: ").strip()
#     all_products = product_manager.read()
#     new_products = []
#     for product in all_products:
#         if product['name'].lower() != name.lower():
#             new_products.append(product)
#     product_manager.write(new_products)
#     print('Product deleted successfully!')
#     return show_admin_menu()
#
#
# ####################################################################################################
#
# def show_products_beauty(products):
#     text = ""
#     step = 1
#     for product in products:
#         text += f"{product['name']} - {product['price']}"
#         if step % 3 == 0:
#             text += "\n"
#         else:
#             text += "\t | \t"
#         step += 1
#     return text
#
#
# def check_product(name, products):
#     for product in products:
#         if product['name'].lower() == name.lower():
#             return product
#     return False
#
#
# def active_student() -> Union[dict, bool]:
#     students = student_manager.read()
#     for student in students:
#         if student['is_login']:
#             return student
#     return False
#
#
# def update_student_coin(student, total_price):
#     students = student_manager.read()
#
#     index = 0
#     while index < len(students):
#         if students[index]['student_id'] == student['student_id']:
#             students[index]['coin'] -= total_price
#             student_manager.write(students)
#             return True
#         index += 1
#     student_manager.write(students)
#     return True
#
#
# def update_product_quantity(product, quantity):
#     products = product_manager.read()
#
#     index = 0
#     while index < len(products):
#         if products[index]['name'] == product['name']:
#             products[index]['quantity'] -= quantity
#             product_manager.write(products)
#             return True
#         index += 1
#     product_manager.write(products)
#     return True
#
#
# def buy_product():
#     student = active_student()
#     if not student:
#         print("You have to login to buy the product")
#         return show_auth_menu()
#
#     products = product_manager.read()
#     result = show_products_beauty(products)
#     print(result)
#
#     name = input("Enter product name: ")
#     product = check_product(name, products)
#     if not product:
#         print("Sorry, there is no such product, try again")
#         buy_product()
#
#     quantity = int(input(f"How many want to buy from -> {product['name']}: "))
#     if product['quantity'] < quantity:
#         print(f"We do not have enough products, we have {product['quantity']} !")
#         buy_product()
#
#     if student['coin'] < quantity * product['price']:
#         print("You do not have enough coin, sorry !")
#         buy_product()
#
#     total_price = product['price'] * quantity
#     update_student_coin(student, total_price)
#     update_product_quantity(product, quantity)
#
#     order_dict = {
#         "student_id": student['student_id'],
#         "product_name": product['name'],
#         "quantity": quantity,
#         "total_price": total_price,
#         "date": str(datetime.now().date())
#     }
#     order_manager.add_data(order_dict)
#     print("You order successfully created !")
#
#     return show_menu()
#
#
# def show_my_orders():
#     student = active_student()
#     orders = order_manager.read()
#     found = False
#     for order in orders:
#         if str(order['student_id']) == str(student['student_id']):
#             text = f"""
# Student ID: {order['student_id']}
# Name: {order['product_name']}
# Quantity: {order['quantity']}
# Price: {order['total_price']}
# Date: {order['date']}\n
#                     """
#             print(text)
#             found = True
#     if not found:
#         print("You do not have any orders !")
#     return show_menu()
#
#
# def show_admin_menu():
#     text = """
#         1. Add product:
#         2. Delete product:
#         3. Logout:
#     """
#     print(text)
#
#     user_input = input("Enter your choice: ")
#     if user_input == "1":
#         add_product()
#     elif user_input == "2":
#         delete_product()
#
#
# def show_menu():
#     text = """
#     1. Buy product:
#     2. My orders:
#     3. Logout:
# """
#     print(text)
#
#     user_input = input("Enter your choice: ")
#     if user_input == "1":
#         buy_product()
#     elif user_input == "2":
#         show_my_orders()
#     elif user_input == "3":
#         logout_all()
#         return show_auth_menu()
#     else:
#         print("Good bye !")
#         return
#
#
# def show_auth_menu():
#     text = """
#     1. Register
#     2. Login
#     3. Exit
# """
#     print(text)
#
#     user_input = input("Enter your choice: ")
#     if user_input == "1":
#         register()
#     elif user_input == "2":
#         login()
#     elif user_input == "3":
#         print("Good bye !")
#         return
#     else:
#         print("Wrong choice !")
#         return show_auth_menu()
#
#
# if __name__ == "__main__":
#     logout_all()
