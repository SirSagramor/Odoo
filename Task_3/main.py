"""
    Task 3:
    Необхідно розрахувати кількість “обраних” квитків із заданою сумою цифр,
    серед тих, номер яких складається з 2N розрядів.
    'Обраним' є квиток у  якого сума перших N цифр рівна сумі останніх N цифр.
"""


def tickets(n, amount):
    from itertools import combinations_with_replacement
    from math import factorial
    # all combinations where sum of the combinate is equal amount  
    comb = list(filter(lambda x: sum(x) == amount / 2, combinations_with_replacement(range(amount + 1), n)))

    permutations = 0
    # all permutations of the combinations
    for i in comb:
        permutations += factorial(n) / factorial(n - len(set(i)) + 1)

    # combinations of the left and right side 
    return int(permutations ** 2)


n, amount = map(int, input().split())

print(tickets(n, amount))
