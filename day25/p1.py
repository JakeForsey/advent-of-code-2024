with open("day25/input.txt", "r") as f:
    data = f.read().strip()

keys = set()
locks = set()

for block in data.split("\n\n"):
    lines = block.splitlines()
    counts = [-1] * len(lines[0])
    
    for line in lines:
        for i, c in enumerate(line):
            counts[i] += c == "#"

    if "#" in lines[0]:
        locks.add(tuple(counts))
    else:
        keys.add(tuple(counts))

total = 0
for key in keys:
    for lock in locks:
        if all(a + b < 6 for a, b in zip(key, lock)):
            total += 1

print(total)
