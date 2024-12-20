from collections import defaultdict
import heapq
import sys

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

with open("day20/input.txt", "r") as f:
    data = f.read()

walls = set()
sx = sy = ex = ey = None
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        if c == "S":
            sx, sy = x, y
        elif c == "E":
            ex, ey = x, y
        elif c == "#":
            walls.add((x, y))

width = len(line)
height = len(data.splitlines())

frontier = defaultdict(lambda: sys.maxsize)
stack = [(0, sx, sy)]
while stack:
    cost, x, y = heapq.heappop(stack)

    if frontier[(x, y)] < cost:
        continue
    frontier[(x, y)] = cost

    if (x, y) == (ex, ey):
        frontier = dict(frontier)
        break

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        ncost = cost + 1
        if nx not in range(width) or ny not in range(height):
            continue
        if (nx, ny) not in walls:
            heapq.heappush(stack, (ncost, nx, ny))

cheats = defaultdict(set)
for i, ((x0, y0), scost) in enumerate(frontier.items()):
    seen = set()
    stack = [(0, x0, y0)]
    while stack:
        cost, x, y = heapq.heappop(stack)
        
        if cost > 20:
            continue

        if (x, y) in seen:
            continue
        seen.add((x, y))

        if (x, y) in frontier and cost > 0:
            saving = frontier[(x, y)] - scost - cost
            if saving >= 100:
                cheats[saving].add((x, y, x0, y0))
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            ncost = cost + 1
            if nx not in range(width) or ny not in range(height):
                continue
            heapq.heappush(stack, (ncost, nx, ny))

print(sum(len(cheat) for cheat in cheats.values()))
