from string import ascii_lowercase
import random

def random_str(digits=7):
    return "".join([random.choice(ascii_lowercase) for _ in range(digits)])