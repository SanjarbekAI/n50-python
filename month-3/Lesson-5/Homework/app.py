"""
Product: nomili base class yarating
Electronics, Book and Clothing nomili subclass lar ham yarating

base class ni calculate_total_price() nomli method bor bo'lsin va hamma productlarni umumiy narxini chiqarsin
Electronics, Book and Clothing -> bu class lar Product dan voris olsin va ularni ham calculate_total_price()
    nomli methodi bo'lsin lekin ularni har biri o'zini turidagi mahsulotlarni narxini hisoblasin

Product class attributes: name, price
Book attributes: name, price, type, pages
Clothing attributes: name, price, type, color
Electronics attributes: name, price, type, made_in, year

type ni user kiritmaydi qaysi class dan object yasab turganingizga qarab unga default qiymat berasi

Har bir class ni add_to_file() nomli method bor bo'lsin qachonki uni chaqirsam objectni products.json nomli
faylga qo'shib ketsin

har birinini show_data() methodi bo'lishi kerak

Hech qanday menyu yasash shart emas, class dan object yasab ularni methodlarini tekshirib ko'rsangiz bo'ldi

products.json, file strukturasi uchun
[
    {
        "type": "book",
        "name": "The peace and war",
        "price": 12000,
        "pages": 120,
    },
    {
        "type": "electronics",
        "name": "Iphone 12 pro max",
        "price": 12000000,
        "made_in": "China",
        "year": 2024
    },
    {
        "type": "book",
        "name": "The peace and war",
        "price": 12000,
        "color": 120,
    }
]
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def age(self):
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def sound(self):
        raise NotImplementedError("Not implemented")


class Cat(Animal):
    def sound(self):
        return "Meow"

    def age(self):
        return 220




