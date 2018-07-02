"""
    Task 1:
    Створити функцію що приймає число, перевіряє його та виводить “Even” або “Odd”
"""

# parity check function
def oddOrEven(num):
    return "Odd" if num % 2 else "Even"

# Odd
print(oddOrEven(5))
# Even
print(oddOrEven(142))