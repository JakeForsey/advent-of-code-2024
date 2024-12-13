with open("day12/input.txt", "r") as f:
    data = f.read()

i = 0
char_map = {}
grid = {}
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        if c not in char_map:
            char_map[c] = i
            i += 1
        grid[(x, y)] = char_map[c]

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

areas = {tuple(sorted(area)) for area in areas_lookup.values()}

def count_sides(area):
    minx = min(x for x, y in area)
    miny = min(y for x, y in area)
    
    maxx = max(x for x, y in area) + 1
    maxy = max(y for x, y in area) + 1

    below = 0
    for y in range(miny, maxy):
        inside = False
        for x in range(minx, maxx):
            in_area = (x, y) in area
            on_edge = (x, y + 1) not in area
            if in_area and on_edge and not inside:
                below += 1
            if in_area and on_edge:
                inside = True
            else:
                inside = False

    above = 0
    for y in range(miny, maxy):
        inside = False
        for x in range(minx, maxx):
            in_area = (x, y) in area
            on_edge = (x, y - 1) not in area
            if in_area and on_edge and not inside:
                above += 1
            if in_area and on_edge:
                inside = True
            else:
                inside = False

    right = 0
    for x in range(minx, maxx):
        inside = False
        for y in range(miny, maxy):
            in_area = (x, y) in area
            on_edge = (x + 1, y) not in area
            if in_area and on_edge and not inside:
                right += 1
            if in_area and on_edge:
                inside = True
            else:
                inside = False
    
    left = 0
    for x in range(minx, maxx):
        inside = False
        for y in range(miny, maxy):
            in_area = (x, y) in area
            on_edge = (x - 1, y) not in area
            if in_area and on_edge and not inside:
                left += 1
            if in_area and on_edge:
                inside = True
            else:
                inside = False

    return left + right + above + below

total = 0
for i, area in enumerate(areas):
    sides = count_sides(area)
    total += sides * len(area)

print(total)
