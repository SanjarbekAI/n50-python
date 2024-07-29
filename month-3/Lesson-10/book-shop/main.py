# from users import logout_all
# from users import register, login
# from admin import add_book
# from json_manager import books_manager
# from books import show_books
#
#
# def show_admin_menu():
#     text = """
#         1. Add book:
#         2. Update book quantity:
#         3. Delete book:
#         4. Search book with name:
#         5. Show all orders:
#         6. Show all users:
#         7. Logout:
#     """
#     print(text)
#
#     user_input = input("Enter your choice: ")
#     if user_input == "1":
#         if not add_book():
#             print("Book not added")
#         show_admin_menu()
#
#     elif user_input == "2":
#         pass
#
#
# def show_menu():
#     text = """
#     1. Buy book:
#     2. My orders:
#     3. Show all books:
#     4. Search book with name:
#     3. Logout:
# """
#     print(text)
#
#     user_input = input("Enter your choice: ")
#     if user_input == "1":
#         pass
#     elif user_input == "2":
#         pass
#     elif user_input == "3":
#         books = books_manager.read()
#         show_books(books)
#         show_menu()
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
#         if register():
#             show_auth_menu()
#
#     elif user_input == "2":
#         data = login()
#         if data['success'] and data['is_admin']:
#             show_admin_menu()
#         elif data['success'] and data['is_admin'] is False:
#             show_menu()
#         else:
#             show_auth_menu()
#
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
#     show_auth_menu()
