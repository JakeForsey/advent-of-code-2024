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

def display(positions):    
    for y in range(height):
        print(f"{y:>4}", end="")
        for x in range(width):
            symbol = positions.get((x, y), ".")
            print(symbol, end="")
        print()

T = 0
max_center = 0
while True:
    T += 1
    positions = Counter([
        (
            (px + (vx * T)) % width,
            (py + (vy * T)) % height,
        )
        for px, py, vx, vy in robots
    ])

    center = sum((x, 39) in positions for x in range(width))
    if center > max_center:
        max_center = center
        display(positions)
        print(T)
        input()
