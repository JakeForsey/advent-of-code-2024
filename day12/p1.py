with open("day12/input.txt", "r") as f:
    data = f.read()

grid = {}
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        grid[(x, y)] = c

areas_lookup = {}
stack = [(x, y, set([(x, y)])) for (x, y) in grid.keys()]
while stack:
    x, y, area = stack.pop(-1)
    areas_lookup[(x, y)] = area

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = dx + x, dy + y
        if (nx, ny) not in grid:
            continue
        if (nx, ny) in area:
            continue
        if grid[(nx, ny)] != grid[(x, y)]:
            continue
        
        area.add((nx, ny))
        stack.append((nx, ny, area))

total = 0
for area in {tuple(sorted(area)) for area in areas_lookup.values()}:
    perimiter = 0
    for x, y in area:
        c = grid[(x, y)]
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = dx + x, dy + y
            if (nx, ny) not in grid or grid[(nx, ny)] != c:
                perimiter += 1
    
    total += perimiter * len(area)
print(total)
