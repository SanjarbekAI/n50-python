from json_manager import books_manager


class Book:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = quantity


def show_books(books: list):
    if len(books) == 0:
        print("There are no books")
    else:
        text = "No\t | Name\t | Price\t | Quantity\n"
        counter = 1
        for book in books:
            text += f"{counter}\t | {book['name']}\t  | {book['price']}\t | {book['quantity']}\n"
        print(text)
