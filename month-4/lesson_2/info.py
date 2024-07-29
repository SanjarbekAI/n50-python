"""
- Decorators
- static, class, instance methods and property
"""

"""
O'quvchilarni baholash sistemasini tuzish kerak.

O'qituvchi har bir o'quvchini bahosini qo'yganda va o'zgartirganda, shu haqidagi malumotni birorta
faylga yozib ketish kerak.

Baho qo'yish uchun faqatgina o'qituvchi bo'lishi kerak. Hatto admin ham baholarni o'zgartira olmaydi.

Sizda jami 3 ta turdagi foydalanuvchilar bor bo'ladi.

1. admin
2. teacher
3. student

Auth menu:
    - Login
    - Exit

Admin menu:
    - fan qo'shish -> name, duration, price
    - fanlarni ro'yxatini ko'rish va o'chirish va o'zgartirish
    - o'qituvchi qo'shish -> full_name, phone_number(unique), subject
    - o'qituvchilarni ko'rish va o'chirish
    - guruh yaratish -> name(unique), teacher, total_student
    - studentni guruhga qo'shish -> group_name, phone_number
    - studentni guruhdan olib tashlash -> group_name, phone_number
    - hamma studentlarni ko'rish va o'chirish
    - Logout

Teacher menu:
    - mening guruhlarim
    - guruh bo'yicha o'quvchilar ro'yxatini ko'rish
    - baholash -> student_phone_number, grade
    - bahosini o'zgartirish -> student_phone_number, grade
    - Logout


Student menu:
    - mening fanlarim
    - mening baholarim
    - Logout
"""



