import random

def flip_coin():
    return "Heads" if random.choice([True, False]) else "Tails"


result = flip_coin()
print(f"The coin landed on: {result}")
