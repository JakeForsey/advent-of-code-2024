with open("day04/input.txt", "r") as f:
    data = f.read()

lines = data.splitlines()
grid = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[(x, y)] = c

count = 0
for x in range(len(line)):
    for y in range(len(lines)):
        
        for dx, dy in [
            (0, 1),
            (1, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]:
            xi = x
            yi = y
            for c in "XMAS":
                if c != grid.get((xi, yi)):
                    break
                if c == "S":
                    count += 1
                xi += dx
                yi += dy

print(count)