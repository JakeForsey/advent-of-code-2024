with open("day15/input.txt", "r") as f:
    data = f.read()

grid_str, directions_str = data.split("\n\n")

sx, sy = None, None
boxes = set()
walls = set()
for y, line in enumerate(grid_str.splitlines()):
    for x, c in enumerate(line):
        if c == "@":
            sx, sy = x, y
        elif c == "O":
            boxes.add((x, y))
        elif c == "#":
            walls.add((x, y))

directions = []
for c in directions_str.replace("\n", ""):
    if c == ">":
        directions.append((1, 0))
    elif c == "v":
        directions.append((0, 1))
    elif c == "<":
        directions.append((-1, 0))
    elif c == "^":
        directions.append((0, -1))

x, y = sx, sy
for dx, dy in directions:

    blocked = False
    ray = []
    rx, ry = x + dx, y + dy
    for i in range(1000):
        if (rx, ry) in walls:
            blocked = True
            break
        if (rx, ry) in boxes:
            ray.append((rx, ry))
        else:
            break
        rx, ry = rx + dx, ry + dy
    
    if not blocked:
        for bx, by in ray:
            boxes.remove((bx, by))
        for bx, by in ray:
            boxes.add((bx + dx, by + dy))
        x, y = x + dx, y + dy

total = 0
for bx, by in boxes:
    total += bx + (by * 100)

print(total)
