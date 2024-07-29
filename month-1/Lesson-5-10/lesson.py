"""
1. 1 dan 1000 oralig`idagi 5 ta bo`luvchilari bor sonlarni toping.
2. Karra jadvalini chiqarib bering. 
3. Agar berilgan soni o`ngdan chapga va chapdan o`ngga bir xil o`qilsa palindrom deb ataymiz. 
100 dan kichik palindrom sonlarni toping.
4. Foydalanuvchi m va n sonlarini kiritadi. 1 n gacha bo'lgan sonlar orasida kvadirati m dan 
katta bo'lgan 1-sonni toping
5. 1 dan 1000 gacha bo`lgan n soni va m soni berilgan. n va m sonlari
kvadratining ayirmasini chiqaring.

8. Ikki natural sonning umumiy bo'linuvchilarini eng kichigini topuvchi
dastur tuzing.
9. 1 dan 100 gacha raqamlari yig'indisi 3 ga karra bo'lgan sonlarni print qiling
10. Foydalanuvchi sizga vaqtni sekund birligida kiritadi, siz unga usha vaqtni necha
kun, soat, minut, daqiqa, sekund borligini ko'rsatasiz
s 

"""
# res = 1
# for i in range(-80, 80):
#     if i % 7 == 0 and i % 2 == 1:
#         res *= i
# print(res)


"""
000 000 | 999 999
"""
# counter = 0
# for a in range(10):
#     for b in range(10):
#         for c in range(10):
#             print(a, b, c)
#             if a + b + c == 13:
#                 counter += 1

# print(counter)

# counter = 0

# n = int(input("son: "))

# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)



# num = int(input("Num: "))
# i = num // 2

# while i > 0:
#     if num % i == 0:
#         print(i)
#     i -= 1


# num = input("Num: ") #34321
# digits = "3421"

# for i in num:
#     if i not in digits:
#         digits += i

# print(len(digits))

i = 2
while i < 10:
    j = 2
    while j < 10:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1
    print(end="\n")

