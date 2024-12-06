with open("day06/input.txt") as f:
    data = f.read()

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]

GRID = {}
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        if c == "^":
            START_X, START_Y = x, y
            c = "."
        GRID[(x, y)] = c

def run(obstacle) -> tuple[bool, set[int, int, int, int]]:
    x, y = START_X, START_Y
    dx, dy = DIRECTIONS[0]
    visited = set()
    visited.add((x, y, dx, dy))
    while True:
        nx, ny = x + dx, y + dy

        if (nx, ny) not in GRID:
            return False, visited
        
        if GRID[(nx, ny)] == "#" or (nx, ny) == obstacle:
            index = DIRECTIONS.index((dx, dy))
            dx, dy = DIRECTIONS[index + 1]
            continue

        x, y, = nx, ny

        state = x, y, dx, dy
        if state in visited:
            return True, visited

        visited.add(state)

_, visited = run(None)
candidates = {(x, y) for x, y, _, __ in visited}
print(sum(run(candidate)[0] for candidate in candidates))
