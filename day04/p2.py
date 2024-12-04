with open("day04/input.txt", "r") as f:
    data = f.read()

lines = data.splitlines()
grid = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[(x, y)] = c

INDEXES = [
    (-1, -1),
    (1, -1),
    (-1, 1),
    (1, 1),
]
PATTERNS = [
    ("M", "M", "S", "S"),
    ("M", "S", "M", "S"),
    ("S", "M", "S", "M"),
    ("S", "S", "M", "M"),
]
count = 0
for x in range(len(line)):
    for y in range(len(lines)):
        if grid[(x, y)] != "A":
            continue
        pattern = tuple(
            grid.get((x + dx, y + dy))
            for dx, dy in INDEXES
        )
        if pattern in PATTERNS:
            count +=1

print(count)
