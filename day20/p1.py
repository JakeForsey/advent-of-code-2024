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
for (x, y), scost in frontier.items():
    for dx, dy in DIRECTIONS:
        x1, y1 = dx + x, dy + y
        if (x1, y1) in frontier:
            saving = frontier[(x, y)] - scost - 1
            if saving >= 100:
                cheats[saving].add((x, y, x1, y1))

        for dx, dy in DIRECTIONS + [(0, 0)]:
            x2, y2 = dx + x1, dy + y1
            if (x2, y2) in frontier:
                saving = frontier[(x2, y2)] - scost - 2
                if saving >= 100:
                    cheats[saving].add((x, y, x2, y2))

print(sum(len(cheat) for cheat in cheats.values()))
