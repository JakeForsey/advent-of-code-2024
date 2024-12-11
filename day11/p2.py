from collections import defaultdict
from functools import lru_cache

@lru_cache()
def step(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        snum = str(num)
        mid = len(snum) // 2
        return [int(snum[:mid]), int(snum[-mid:])]
    else:
        return [num * 2024]

with open("day11/input.txt", "r") as f:
    data = f.read()

nums = {int(c): 1 for c in data.split()}

for blink in range(75):
    next_nums = defaultdict(int)
    for num, count in list(nums.items()):
        new_nums = step(num)
        for new_num in new_nums:
            next_nums[new_num] += count
    nums = next_nums

print(sum(count for count in nums.values()))
