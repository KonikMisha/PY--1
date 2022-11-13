import random


def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    spisok = []
    while len(spisok) < 16:
        a = random.randint(-10,10)
        if a not in spisok:
            spisok.append(a)
    return spisok
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
