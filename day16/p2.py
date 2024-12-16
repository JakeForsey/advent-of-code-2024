from collections import defaultdict

EAST = (1, 0)
WEST = (-1, 0)
NORTH = (0, -1)
SOUTH = (0, 1)

FORWARD = {
    EAST: EAST,
    WEST: WEST,
    NORTH: NORTH,
    SOUTH: SOUTH,
}
CLOCKWISE = {
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH,
    NORTH: EAST,
}
COUNTER_CLOCKWISE = {b: a for a, b in CLOCKWISE.items()}

with open("day16/input.txt", "r") as f:
    data = f.read()

sx, sy = None, None
ex, ey = None, None
walls = set()
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        if c == "#":
            walls.add((x, y))
        elif c == ".":
            continue
        elif c == "E":
            ex, ey = x, y
        elif c == "S":
            sx, sy = x, y
        else:
            raise AssertionError("Unreachable")

def forward(x, y, dx, dy):
    return x + dx, y + dy, dx, dy

def clockwise(x, y, dx, dy):
    dx, dy = CLOCKWISE[(dx, dy)]
    return x, y, dx, dy

def counter_clockwise(x, y, dx, dy):
    dx, dy = COUNTER_CLOCKWISE[(dx, dy)]
    return x, y, dx, dy

best_paths = []
state_costs = defaultdict(lambda: float("inf"))
min_cost = float("inf")
stack = [(sx, sy, *EAST, 0, {(sx, sy)})]
while stack:
    x, y, dx, dy, cost, path = stack.pop(0)

    if (x, y) == (ex, ey):
        if cost < min_cost:
            min_cost = cost
            best_paths = [path]
        if cost == min_cost:
            best_paths.append(path)
        continue

    for ncost, action in [
            (1, forward),
            (1000, clockwise),
            (1000, counter_clockwise)
        ]:
        nx, ny, ndx, ndy = action(x, y, dx, dy)
        ncost = cost + ncost

        if ncost > min_cost:
            # A cheaper end to end route already found
            continue

        if (nx, ny) in walls:
            continue
        
        if ncost > state_costs[(nx, ny, ndx, ndy)]:
            # A cheaper way to this state already found
            continue
        state_costs[(nx, ny, ndx, ndy)] = ncost
        
        npath = path.copy()
        npath.add((nx, ny))
        stack.append((nx, ny, ndx, ndy, ncost, npath))

tiles = set()
for path in best_paths:
    tiles |= path
print(len(tiles))
