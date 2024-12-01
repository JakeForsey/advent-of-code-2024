with open("day01/input.txt", "r") as f:
    data = f.read()

lefts, rights = [], []
for line in data.splitlines():
    left, right = line.split("   ")
    left, right = int(left), int(right)
    lefts.append(left)
    rights.append(right)

lefts.sort()
rights.sort()

print(sum(abs(l -r) for l, r in zip(lefts, rights)))