"""
Bugungi savollar ?

1. Variable lar qanday yaratiladi va ishlaydi ?
2. Dynamic typing language nima ?
3. Memory wanday ishlaydi ?
4. Immutable and Mutable bularni farqlari nimada ?
5. None qanday ishlaydi ?
6. Listni xotirada qanday saqlaydi ?
7. == and is farqlari nimada ?
8. Funksiya parametrlari qanday ishlaydi ?
9. Nima uchun ularni parametr va argumentlarni bir xil nomlash yaxshi emas ?

- References
- Dynamic typing
- Garbage collection
- mutable& immutable objects
- is operator
- None

Useful videos:
- https://youtu.be/mMbVs17Vmo4
-
"""

"""
Mashq qilish uchun masala:

Masala: 1
Hurmatli o'quvchi sizni vazifangiz sirli chat qilish uchun dastur tuzish.
Yani men dasturga kiraman va kod bilan chat yaratman, va dastur menda ID beradi
Keyin men shu ID ni sherigimga aytsam u mana shu chatga qo'shiladi. Va u yozgan habarlar menda 
men yozgan habarlarim unda ko'rinishi kerak. Chatni yaratgan odam chatni yopsa hamma narsa o'chib 
ketishi kerak. OMAD.


Masala: 2
Najot ta'limda yangi kurslar ochish, kurslarga o'quvchilarni qo'shish uchun sistema tuzish kerak.
Unda 3 ta turdagi foydalanuvchilar bo'ladi.
1. Super admin -> boshqa adminlarni qo'sha oladi
2. Admin -> kurslarni yaratadi, kursga o'quvchini qo'shadi, o'chiradi
3. Student -> o'zini ID va login bilan kiradi o'zi qo'shilgan kurslarni ko'radi
           -> yoki ma'lum bir vaqt orag'i bo'yicha yangi kurslarni qidirishi mumkin
           

"""

import random


def random_numbers(nums=None):
    if nums is None:
        nums = []
        nums.append(random.randint(1, 10))
    nums.append(random.randint(1, 10))
    return nums


"""
random_numbers
def_arg = nums[3, 4]
"""
