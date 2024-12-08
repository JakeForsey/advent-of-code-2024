from collections import defaultdict

with open("day08/input.txt", "r") as f:
    data = f.read()

lines = data.splitlines()
antenna_groups = defaultdict(set)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ".":
            antenna_groups[c].add((x, y))

width, height = len(line), len(lines)

antinodes = set()
for group, antennas in antenna_groups.items():
    for antenna in antennas:
        for other in antennas:
            if antenna == other:
                continue

            antinodes.add(other)
            antinodes.add(antenna)

            for i in range(1, height):
                dx = (antenna[0] - other[0]) * i
                dy = (antenna[1] - other[1]) * i

                antinode1 = antenna[0] + dx, antenna[1] + dy
                antinode2 = other[0] - dx, other[1] - dy
                
                if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                    antinodes.add(antinode1)
                
                if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                    antinodes.add(antinode2)

print(len(antinodes))
