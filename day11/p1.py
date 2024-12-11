with open("day11/input.txt", "r") as f:
    data = f.read()

nums = [int(c) for c in data.split()]

def step(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        snum = str(num)
        mid = len(snum) // 2
        return [int(snum[:mid]), int(snum[-mid:])]
    else:
        return [num * 2024]

for blink in range(25):
    next_nums = []
    for num in nums:
        next_nums.extend(step(num))
    nums = next_nums

print(len(nums))
