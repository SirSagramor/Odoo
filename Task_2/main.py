'''
    Task 2:
    Ваша програма має видати безперервну послідовність латинських літер в нижньому регістрі довжиною 1 000 000 символів.
    Послідовність має відповідати вимогам:
        -Кожна літера з'являється не частіше 40 000 раз в послідовності;
        -Кожна можлива послідовність з двох букв зявляється не частіше 2 000;
        -Кожна можлива послідовність з трьох букв з'являється не частіше 100;
'''


# function for check sequence
def checkSequence(combinations):
    for key in combinations:
        if len(key) == 1:
            if combinations[key] > 40000:
                print("Problem with one letter")
        elif len(key) == 2:
            if combinations[key] > 2000:
                print("Problem with double sequence")
        elif len(key) == 3:
            if combinations[key] > 100:
                print("Problem with triple sequence")
        else:
            print("Problem with keys")


# function for finding the sequence
def sequenceLetters():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # combinations in text
    combinations = {}
    text = ''

    for i in range(1000000):
        for c in alphabet:
            if i == 0:
                text += c
                combinations[c] = 1
                break
            elif i == 1:
                text += c
                combinations[c] = 1
                combinations[text[i - 1] + c] = 1
                break
            if c in combinations and (text[i - 1] + c) in combinations and (text[i - 2:i] + c) in combinations:
                if combinations[c] >= 40000 or combinations[text[i - 1] + c] >= 2000 or combinations[text[i - 2:i] + c] >= 100:
                    continue
                combinations[c] += 1
                combinations[text[i - 1:i] + c] += 1
                combinations[text[i - 2:i] + c] += 1
                text += c
                break
            else:
                if not c in combinations:
                    combinations[c] = 1
                    text += c
                    break
                elif combinations[c] < 40000 and not ((text[i - 1] + c) in combinations):
                    combinations[c] += 1
                    combinations[text[i - 1:i] + c] = 1
                    text += c
                    break
                elif combinations[c] < 40000 and combinations[text[i - 1] + c] < 2000 and not((text[i - 2:i] + c) in combinations):
                    combinations[c] += 1
                    combinations[text[i - 1] + c] += 1
                    combinations[text[i - 2:i] + c] = 1
                    text += c
                    break
        # change alphabet
        alphabet = alphabet[1:] + alphabet[0]

    checkSequence(combinations)
    return text


my_sequence = sequenceLetters()
print(my_sequence)


