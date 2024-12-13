from z3 import Int, Optimize, sat

with open("day13/input.txt", "r") as f:
    data = f.read()

def parse_position(text, offset=0):
    _, xy = text.split(":")
    x, y = xy.split(", ")
    return (
        int(x.replace("X", "").replace("=", "")) + offset,
        int(y.replace("Y", "").replace("=", "")) + offset,
    )

total = 0
for block in data.split("\n\n"):
    button_a, button_b, prize = block.splitlines()
    ax, ay = parse_position(button_a)
    bx, by = parse_position(button_b)
    x, y = parse_position(prize, offset=10000000000000)
    a = Int('a')
    b = Int('b')
    solver = Optimize()
    solver.add(a * ax + b * bx == x)
    solver.add(a * ay + b * by == y)
    solver.minimize(a * 3 + b)
    if solver.check() == sat:
        model = solver.model()
        cost = model.eval(a * 3 + b).as_long()
        total += cost

print(total)
