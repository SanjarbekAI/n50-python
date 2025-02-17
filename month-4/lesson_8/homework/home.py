"""
Tasavvur qiling Najot Ta'limda yangiliklarni email orqali olish imkoni
paydo bo'ldi. Ya'ni qandaydir yangilik bo'lsa sizga kiritgan email
akauntingiz uchun habar kelib turadi.

Sizni vazifangiz shunga o'xshash dastur yaratish. Ya'ni men dasturni ishga tushurganimda u menda
login, register so'raydi. Ro'yxatdan o'tish uchun men email akauntimni kiritaman va tasdiqlayman.
Va menga kelgan habarlarni ko'rib turishim mumkin bo'ladi.

Agar admin bo'lsam menda hamma foydalanuvchilarni ko'rish, va ularga gmail orqali
habar yuborish imkoni bo'lishi kerak. Habarlarni ushbu kategorilar orqali yuborishim
mumkin:
0. Hamma uchun
1. Faqat qizlar uchun habar
2. Faqat yigitlar uchun habar
3. 18 yoshdan kattalar uchun
4. 18 yoshdan kichiklar uchun

Foydalanuvchi ro'yxatdan o'tayotgan vaqtida ismini, yoshini, jinsini, gmail, parol malumotlarini kiritadi.


Auth menu:
    - Register
        - gmail, password, confirm_password, full_name, age, gender
    - Login
        - gmail, password
    - Exit


Admin menu:
    - show all users | if you use generator to print users data (ijson)
    - send message from gmail:
        0. To all users
        1. To males
        2. To females
        3. Higher from 18
        4. Lower from 18
    - show sent message with time
    - Logout

User menu:
    - show all new messages
    - show all read messages
    - Logout
"""