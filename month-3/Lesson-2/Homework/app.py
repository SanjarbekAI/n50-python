"""
Tomoshabinlar konsertga bilet sotib olishlari uchun quyidagicha dastur yozing:
    Class Concert: author, date, total_tickets, price
    Methods:
        get_price()
        get_full_info()
        buy_ticket(full_name, phone_number, quantity)
        save_to_file()
        available_tickets_count()
        sold_tickets_count()
        read_data()
        User bilet olgandan keyin total_tickers kamayib borishi kerak, agar bilet tugasa sotib ola olmaydi
"""


class Concert:
    def __init__(self, author, date, total_tickets, price):
        self.author = author
        self.date = date
        self.total_tickets = total_tickets
        self.price = price

    def get_price(self):
        return self.price

    def available_tickets_count(self):
        return self.total_tickets

    def buy_ticket(self, full_name, phone_number, quantity):
        if quantity <= self.total_tickets:
            self.total_tickets -= quantity
        else:
            return f"Sorry, you don't have enough tickets, we have {self.available_tickets_count()}"
        # add to file

# concert1 = Concert("botir qodirov", '2024-06-26', 50000, 50000)
# print(concert1.available_tickets_count())
# concert1.buy_ticket("sa", "sa", 49999)
# print(concert1.available_tickets_count())



