"""
Balli, Malades, Shapaloq

348

123
Shapaloq Shapaloq Balli

"""

import random

random_num = str(random.randint(100, 999))


attemps = 5

while attemps > 0:
    user_num = input("Enter number: ")
    first = user_num[0]
    second = user_num[1]
    third = user_num[2]

    text = ""

    if random_num == user_num:
        print("Yutdingiz !")
        break
    if first in random_num and first == random_num[0]:
        text += "Malades "
    elif first in random_num and first != random_num[0]:
        text += "Balli "
    elif first not in random_num:
        text += "Shapaloq "

    if second in random_num and second == random_num[1]:
        text += "Malades "
    elif second in random_num and second != random_num[1]:
        text += "Balli "
    elif second not in random_num:
        text += "Shapaloq "

    if third in random_num and third == random_num[2]:
        text += "Malades "
    elif third in random_num and third != random_num[2]:
        text += "Balli "
    elif third not in random_num:
        text += "Shapaloq "

    
    print(text)
    attemps -= 1
else:
    print(f"You lose {random_num}")
