from collections import Counter

with open("day14/input.txt", "r") as f:
    data = f.read()

height, width = 103, 101
# height, width = 7, 11
robots = set()
for line in data.splitlines():
    p, v = [text.replace("p", "").replace("v", "").replace("=", "") for text in line.split(" ")]
    px, py = map(int, p.split(","))
    vx, vy = map(int, v.split(","))
    robots.add((px, py, vx,vy))

T = 100
positions = Counter([
    (
        (px + (vx * T)) % width,
        (py + (vy * T)) % height,
    )
    for px, py, vx, vy in robots
])

mid_width = width // 2
mid_height = height // 2
total = 1
for x1, x2, y1, y2 in [
    (
        0,
        mid_width,
        0,
        mid_height,
    ),
    (
        mid_width + 1,
        width,
        mid_height + 1,
        height,
    ),
    (
        mid_width + 1,
        width,
        0,
        mid_height,
    ),
    (
        0,
        mid_width,
        mid_height + 1,
        height,
    ),
]:
    quadrant = 0
    for x in range(x1, x2):
        for  y in range(y1, y2):
            quadrant += positions.get((x, y), 0)
    total *= quadrant

print(total)
