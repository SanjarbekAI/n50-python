
def home1(n: int) -> set:
    """
    1 - homework solution.
    Task was "1. 1 dan 100 gacha bo'lsa sonlar uchun raqamlar yig'indisi 5 ga
    karrali bo'lgan sonlar sonini toping. Raqamlar yig'indisi degani
    masalan: 34 => 3 + 4 = 7 "

    :param n:
    :return:
    """
    nums = set()
    for i in range(n):
        j = sum(map(lambda x: int(x), str(i)))
        if j % 5 == 0:
            nums.add(i)

    return nums


def home2(text: str) -> str:
    """
    Solution of homework 2.
    Task was "2. Odamdan ismini kiritishini so'rang va uni ichida inli harflaridan keyin dollar
    belgisini qo'shib qaytarib bering. Masalan: sa$nja$rbe$k "

    :param text:
    :return:
    """
    i = 0
    while i < len(text):
        if text[i] in "aoiue":
            text = f"{text[:i]}${text[i:]}"
            i += 1
        i += 1
    return text


def get_biggest_by_sum_nums(nums: list[int]) -> int:
    """
    The solution of homework 3.
    Task was "3. Odamdan 2 ta son so'rang va raqamlari yig'indisi kattasini qaytaring.
    Masalan: 91 va 67 bo'lsa 9 + 1 = 10 va 6 + 7 = 13 demak 67 ni qaytarasiz.

    :param nums:
    :return:
    """
    return max(nums, key=lambda num: sum(map(lambda char: int(char), str(num))))