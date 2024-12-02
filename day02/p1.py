from math import copysign

with open("day02/input.txt", "r") as f:
    data = f.read()

result = 0
for line in data.splitlines():
    report = list(map(int, line.split()))
    diffs = [a - b for a, b in zip(report, report[1:])]

    same_direction = all(copysign(1, d) == copysign(1, diffs[0]) for d in diffs)
    correct_magnitude = all(abs(d) >= 1 and abs(d) <= 3 for d in diffs)
    safe = same_direction and correct_magnitude
    result += safe

print(result)
