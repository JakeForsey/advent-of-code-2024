from collections import defaultdict

with open("day01/input.txt", "r") as f:
    data = f.read()

lefts, rights = [], defaultdict(int)
for line in data.splitlines():
    left, right = line.split("   ")
    left, right = int(left), int(right)
    lefts.append(left)
    rights[right] += 1

result = 0
for left in lefts:
    result += rights[left] * left

print(result)