with open("day15/input.txt", "r") as f:
    data = f.read()

grid_str, directions_str = data.split("\n\n")

sx, sy = None, None
boxes = {}
walls = set()
y = 0
for line in grid_str.splitlines():
    x = 0
    for c in line.strip():
        if c == "@":
            sx, sy = x, y
        elif c == "O":
            boxes[(x, y)] = (x, y, x + 1, y)
            boxes[(x + 1, y)] = (x, y, x + 1, y)
        elif c == "#":
            walls.add((x, y))
            walls.add((x + 1, y))
        x += 2
    y += 1

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

def connected_boxes(x, y, dx, dy):
    to_move = set()
    seen = set()
    stack = [(x + dx, y + dy)]
    while stack:
        x, y = stack.pop()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        if (x, y) in walls:
            return True, {}
        if (x, y) in boxes:
            x0, y0, x1, y1 = boxes[(x, y)]
            to_move.add((x0, y0, x1, y1))
            stack.append((x0 + dx, y0 + dy))
            stack.append((x1 + dx, y1 + dy))
    return False, to_move

x, y = sx, sy
for dx, dy in directions:
    blocked, to_move = connected_boxes(x, y, dx, dy)
    if not blocked:
        for x0, y0, x1, y1 in to_move:
            del boxes[(x0, y0)]
            del boxes[(x1, y1)]
        for x0, y0, x1, y1 in to_move:
            x0, y0, x1, y1 = x0 + dx, y0 + dy, x1 + dx, y1 + dy
            boxes[(x0, y0)] = (x0, y0, x1, y1)
            boxes[(x1, y1)] = (x0, y0, x1, y1)

        x, y = x + dx, y + dy

total = 0
for bx, by, _, _ in set(boxes.values()):
    total += bx + (by * 100)

print(total)
