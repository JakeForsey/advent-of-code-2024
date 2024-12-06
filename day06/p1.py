from itertools import cycle

with open("day06/input.txt") as f:
    data = f.read()

position = None
grid = {}
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        if c == "^":
            position = (x, y)
            c = "."
        grid[(x, y)] = c

directions = cycle([
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
])
dx, dy = next(directions)
visited = set()
while True:
    next_position = position[0] + dx, position[1] + dy
    if next_position not in grid:
        break
    if grid[next_position] == ".":
        position = next_position
    else:
        dx, dy = next(directions)
        position = position[0] + dx, position[1] + dy
    
    visited.add(position)

print(len(visited))
