from itertools import combinations_with_replacement, permutations
from functools import lru_cache

with open("day22/input.txt", "r") as f:
    data = f.read()

def mix(secret_number, value):
    return secret_number ^ value

def prune(secret_number):
    return secret_number % 16777216

@lru_cache(maxsize=99999999)
def calculate_diffs(secret_number):
    prices = [int(str(secret_number)[-1])]
    for _ in range(2000):
        # Calculate the result of multiplying the secret number by 64. 
        #       Then, mix this result into the secret number.
        #       Finally, prune the secret number.
        secret_number = prune(mix(secret_number, secret_number * 64))

        # Calculate the result of dividing the secret number by 32.
        #       Round the result down to the nearest integer.
        #       Then, mix this result into the secret number. 
        #       Finally, prune the secret number.
        secret_number = prune(mix(secret_number, secret_number // 32))

        # Calculate the result of multiplying the secret number by 2048.
        #       Then, mix this result into the secret number.
        #       Finally, prune the secret number.
        secret_number = prune(mix(secret_number, secret_number * 2048))

        price = int(str(secret_number)[-1])
        prices.append(price)

    diffs = []
    for i in range(len(prices) - 1):
        diffs.append(prices[i + 1] - prices[i])
    
    pattern_to_price = {}
    for i in range(len(diffs) -4):
        pattern = tuple(diffs[i: i + 4])
        # Only keep the first intance of the pattern
        if pattern not in pattern_to_price:
            pattern_to_price[pattern] = prices[i + 4]

    return pattern_to_price

secret_numbers = [int(line) for line in data.splitlines()]

best_total = 0
for combination in combinations_with_replacement(range(-9, 10), 4):
    for permutation in permutations(combination, 4):

        total = 0
        for secret_number in secret_numbers:
            x = calculate_diffs(secret_number)
            total += x.get(permutation, 0)

        if total > best_total:
            best_total = total

print(best_total)
