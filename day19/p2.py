with open("day19/input.txt", "r") as f:
    data = f.read()

patterns_str, designs_str = data.split("\n\n")
patterns = patterns_str.split(", ")

designs = []
for design in designs_str.splitlines():
    designs.append(design)

def pop_min(stack):
    key, value = min(stack.items(), key=lambda x: x[1])
    del stack[key]
    return key, value

possible = 0
for i, design in enumerate(designs):
    stack = {design: 1}
    while stack:
        remaining, count = pop_min(stack)

        if len(remaining) == 0:
            possible += count
            continue
        
        for pattern in patterns:
            if remaining.startswith(pattern):
                next_remaining = remaining[len(pattern):]
                other_counts = stack.get(next_remaining, 0)
                stack[next_remaining] = other_counts + count

print(possible)
