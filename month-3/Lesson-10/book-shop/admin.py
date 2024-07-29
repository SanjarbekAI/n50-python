from json_manager import books_manager
from books import Book


def add_book() -> bool:
    try:
        name = input("Book name: ")
        price = input("Book price: ")
        quantity = input("Book quantity: ")
        book = Book(name, price, quantity)
        books_manager.add_data(book.__dict__)
        print("Book is added")
        return True
    except Exception as e:
        print(f"Error adding product: {e}")
        return False
