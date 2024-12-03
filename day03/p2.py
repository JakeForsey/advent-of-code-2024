import re

with open("day03/input.txt", "r") as f:
    data = f.read().strip()

enabled = True
total = 0
for match in re.findall("(do\(\))|(don't\(\))|mul\(([0-9]+),([0-9]+)\)", data):

    is_do = match[0] != ""
    if is_do:
        enabled = True
        continue

    is_dont = match[1] != ""
    if is_dont:
        enabled = False
        continue

    if enabled:
        total += int(match[2]) * int(match[3])

print(total)
