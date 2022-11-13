import random


def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
    words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upwords = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = words + upwords + numbers
    password = ''
    for i in range(8):
        password = password + symbols[random.randint(0, len(symbols))]
    return password
print(get_random_password())
