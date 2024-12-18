with open("day18/input.txt", "r") as f:
    data = f.read()

# width, height = 6, 6
width, height = 70, 70

walls = set()
for line in data.splitlines()[:1024]:
    x, y = map(int, line.split(","))
    walls.add((x, y))

sx, sy = 0, 0
ex, ey = width, height

frontier = {}
stack = [(sx, sy, 0)]
while stack:
    x, y, cost = stack.pop()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        ncost = cost + 1

        if not (0 <= nx <= width):
            continue
        if not (0 <= ny <= width):
            continue

        if (nx, ny) in walls:
            continue
        
        previous_cost = frontier.get((nx, ny), float("inf"))
        if previous_cost <= ncost:
            continue
        
        frontier[(nx, ny)] = ncost
        stack.append((nx, ny, ncost))

print(frontier[ex, ey])
