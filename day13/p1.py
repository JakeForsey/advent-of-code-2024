with open("day13/input.txt", "r") as f:
    data = f.read()

def parse_position(button_a):
    _, xy = button_a.split(":")
    x, y = xy.split(", ")
    return (
        int(x.replace("X", "").replace("=", "")),
        int(y.replace("Y", "").replace("=", "")),
    )

total = 0
for block in data.split("\n\n"):
    button_a, button_b, prize = block.splitlines()
    ax, ay = parse_position(button_a)
    bx, by = parse_position(button_b)
    x, y = parse_position(prize)
    min_cost = float("inf")
    for a in range(100):
        for b in range(100):
            xx, yy = (a * ax + b * bx, a * ay + b * by)
            if (xx, yy) == (x, y):
                cost = a * 3 + b
                if cost < min_cost:
                    min_cost = cost
    if min_cost != float("inf"):
        total += min_cost

print(total)