# """
# 1. create a base class Vehicle with a method move(). Then, create two subclasses,
#     Car and Boat, each overriding the move() method. Write a function that takes
#     a Vehicle object and calls its move() method.
# """
#
#
# class Vehicle:
#     def move(self):
#         return "vehicle is moving"
#
#
# class Boat(Vehicle):
#     def move(self):
#         return "boat is moving on the water"
#
#
# class Car(Vehicle):
#     def move(self):
#         return "car is running on the road"
#
#
# car1 = Car()
# print(car1.move())

"""
Create a base class DataFormatter with a method format(data: dict).
    Implement subclasses JSONFormatter, TextFormatter, and CSVFormatter,
    each overriding the format() method. Write a function that takes
    a list of DataFormatter objects and calls their format() methods
    with some data.
"""

# import json
# import csv
#
#
# class DataFormatter:
#     def format(self, data):
#         return data
#
#
# class TextFormatter(DataFormatter):
#     def format(self, data):
#         with open("text.txt", "w") as f:
#             f.write(f"{data['name']},{data['age']},{data['city']}\n")
#             return "Data formatted as text"
#
#
# class JSONFormatter(DataFormatter):
#     def format(self, data):
#         with open("json.json", "w") as f:
#             json.dump(data, f, indent=4)
#             return "Data formatted as JSON"
#
#
# class CSVFormatter(DataFormatter):
#     def format(self, data):
#         with open("csv.csv", "w", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow(data.keys())
#             writer.writerow(data.values())
#             return "Data formatted as CSV"
#
#
# def format_data(formatters, data):
#     for formatter in formatters:
#         print(formatter.format(data))
#
#
# if __name__ == "__main__":
#     data = {"name": "John", "age": 30, "city": "New York"}
#     formatters = [TextFormatter(), JSONFormatter(), CSVFormatter()]
#     format_data(formatters, data)


import json, os


class JsonManager:
    file_name = "products.json"

    def check_existence(self):
        return os.path.exists(self.file_name)

    def read_json_file(self):
        if self.check_existence():
            if os.path.getsize(self.file_name) != 0:
                with open(self.file_name, 'r') as file:
                    data = json.load(file)
                    return data
            return []
        return []

    def write_json_file(self, all_data):
        with open(self.file_name, mode='w') as file:
            json.dump(all_data, file, indent=4)
            return "Data is added"

    def add_one_data(self, data: dict):
        all_data = self.read_json_file()
        all_data.append(data)
        return self.write_json_file(all_data)


class Device(JsonManager):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__summa = 0

    def get_total_price(self):
        products = self.read_json_file()
        for product in products:
            self.__summa += product["price"]
        return self.__summa


class Phone(Device):
    def __init__(self, name, price, storage, color):
        super().__init__(name, price)
        self.type = "phone"
        self.storage = storage
        self.color = color
        self.__summa = 0

    def change_to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "storage": self.storage,
            "color": self.color,
            "type": self.type
        }

    def get_total_price(self):
        products = self.read_json_file()
        for product in products:
            if product["type"] == self.type:
                self.__summa += product["price"]
        return self.__summa


class Computer(Device):
    def __init__(self, name, price, made_in, year):
        super().__init__(name, price)
        self.type = "computer"
        self.made_in = made_in
        self.year = year
        self.__summa = 0

    def change_to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "made_in": self.made_in,
            "year": self.year,
            "type": self.type
        }

    def get_total_price(self):
        products = self.read_json_file()
        for product in products:
            if product["type"] == self.type:
                self.__summa += product["price"]
        return self.__summa


phone = Phone(name="Iphone 14", price=1300000, storage="256 GB", color="purple")
print(phone.get_total_price())
# print(phone.add_one_data(phone.change_to_dict()))

computer = Computer(name="macbook m2 air", price=230000, made_in="china", year=2024)
print(computer.get_total_price())
# print(computer.add_one_data(computer.change_to_dict()))