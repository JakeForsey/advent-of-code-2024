with open("day10/input.txt", "r") as f:
    data = f.read()

start_positions = set()
grid = {}
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        value = int(c)
        if value == 0:
            start_positions.add((x, y))
        grid[(x, y)] = value


DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

paths = 0
print(start_positions)
for (x, y) in start_positions:
    seen = set()
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        seen.add((x, y))
        value = grid[(x, y)]
        if value == 9:
            paths += 1
            continue
        for dx, dy in DIRECTIONS:
            nx, ny = dx + x, dy + y
            if (nx, ny) not in grid:
                continue
            nvalue = grid[(nx, ny)]
            if (nvalue - value) != 1:
                continue
            if (nx, ny) in seen:
                continue

            stack.append((nx, ny))

print(paths)