"""
Twitterga o'xshash dastur yasash kerak.
Ma'lumotlarni oddiy txt faylda saqlang.

Auth menu:
    - Register | full_name, username, gmail, password, created_at(automatic)
    - Login    | username, password
    - Exit

User menu:
    - Create a post | message, created_at(automatic)
    - Get my all posts | Postlarni qatorma qator o'qib beradigan generator yozing
    - Logout

Admin menu:
    - Show all users | Foydalanuvchilarni qatorma qator o'qib beradigan generator yozing
    - Show all posts | Birinchi 5 ta postni ko'rsatsin
        - previous -> buni tanlasa oldingi 5 tasini bersin
        - 1/10  -> bu jami nechta page borligi va hozir nechingchi page da ekanligini ko'rsatsin
        - next -> buni tanlasa keyingi 5 tasini bersin
    - Search with keywords | Malum bir so'zlarni ketma ketlikda kiritiladi va shu so'zlar ishtirok
                             etgan barcha postlarni va ularni kim yuklaganligi haqidagi malumotlarni
                             ko'rsatishi kerak
                             Masalan: president, kill, attack
    - Logout
"""

item = [1, 2, 3]
text = "1 2 31, 3, 1"
