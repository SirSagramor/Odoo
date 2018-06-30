"""
    Task 3:
    Необхідно розрахувати кількість “обраних” квитків із заданою сумою цифр,
    серед тих, номер яких складається з 2N розрядів.
    'Обраним' є квиток у  якого сума перших N цифр рівна сумі останніх N цифр.
"""


def tickets(n, summa):
    from itertools import combinations_with_replacement
    from math import factorial

    comb = list(filter(lambda x: sum(x) == summa / 2, combinations_with_replacement(range(summa + 1), n)))

    permutations = 0
    for i in comb:
        permutations += factorial(n) / factorial(n - len(set(i)) + 1)

    return int(permutations ** 2)


n, summa = map(int, input().split())

print(tickets(n, summa))
