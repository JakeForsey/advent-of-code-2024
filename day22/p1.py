with open("day22/input.txt", "r") as f:
    data = f.read()

def mix(secret_number, value):
    return secret_number ^ value

def prune(secret_number):
    return secret_number % 16777216

total = 0
for line in data.splitlines():
    secret_number = int(line)
    
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

    total += secret_number

print(total)
