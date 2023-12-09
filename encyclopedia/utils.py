import random


def generate_captcha():
    num1 = random.randint(5, 10)
    num2 = random.randint(1, 5)
    symbol = random.choice(['+', '-', '*'])
    return f"{num1} {symbol} {num2}"
