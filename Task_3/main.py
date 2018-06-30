"""
    Task 3:
    Необхідно розрахувати кількість “обраних” квитків із заданою сумою цифр,
    серед тих, номер яких складається з 2N розрядів.
    'Обраним' є квиток у  якого сума перших N цифр рівна сумі останніх N цифр.
"""


def tickets(n, summa):
    from itertools import combinations_with_replacement, permutations

    comb = combinations_with_replacement(range(summa + 1), n)
    perm = set()

    for i in comb:
        for j in permutations(i, n):
            perm.add(j)

    amount = 0
    for i in perm:
        if sum(i) == summa / 2:
            amount += 1

    return amount ** 2

n, summa = map(int, input().split())

print(tickets(n, summa))
