from operator import __add__, __mul__

with open("day07/input.txt", "r") as f:
    data = f.read()

result = 0
for line in data.splitlines():
    target, elements = line.split(": ")
    target = int(target)
    elements = list(map(int, elements.split()))

    total = 0
    stack = [(target, elements[0], elements[1:])]
    while stack:
        target, total, remaining = stack.pop()
        if total > target:
            continue
        if target == total and not remaining:
            result += target
            break
        if not remaining:
            continue
        for op in [__add__, __mul__]:
            next_value = remaining[0]
            next_total = op(total, next_value)
            stack.append((target, next_total, remaining[1:]))
    
print(result)
