import re

with open("day03/input.txt", "r") as f:
    data = f.read().strip()

total = 0
for match in re.findall("mul\(([0-9]+),([0-9]+)\)", data):
    total += int(match[0]) * int(match[1])

print(total)
