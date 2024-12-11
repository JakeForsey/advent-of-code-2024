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

paths = set()
print(start_positions)
for (x, y) in start_positions:
    seen = set()
    stack = [(x, y, (x, y))]
    while stack:
        x, y, path = stack.pop()
        seen.add((x, y, path))
        value = grid[(x, y)]
        if value == 9:
            paths.add(path)
            continue
        for dx, dy in DIRECTIONS:
            nx, ny = dx + x, dy + y
            npath = (*path, (nx, ny))
            if (nx, ny) not in grid:
                continue
            nvalue = grid[(nx, ny)]
            if (nvalue - value) != 1:
                continue
            if (nx, ny, npath) in seen:
                continue

            stack.append((nx, ny, npath))

print(len(paths))