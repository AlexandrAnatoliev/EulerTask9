# EulerTask9 - Особая тройка Пифагора

# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
# a**2 + b**2 = c**2
# Например, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

def is_triple(a, b, c):
    """
    Функция, определяющая являются ли введеные числа тройкой Пифагора
    :return: True/False
    """
    return a ** 2 + b ** 2 == c ** 2


def is_sum(a, b, c):
    """
    Функция проверяет числа a,b,c на выполнение условий
    :return: True/False
    """
    return a + b + c == 1000 and a < b < c


for c in range(1000, 0, -1):
    ab = 1000 - c
    for b in range(ab, 0, -1):
        a = ab - b
        if is_sum(a, b, c) and is_triple(a, b, c):
            print(f"Искомые числа: {a}, {b}, {c}")
            print(f"Их произведение: {a * b * c}")
            break
