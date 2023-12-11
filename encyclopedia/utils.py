import random


def get_random_page(obj):
    if obj:
        return random.choice(obj)
    else:
        return None
