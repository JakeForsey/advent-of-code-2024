with open("day19/input.txt", "r") as f:
    data = f.read()

patterns_str, designs_str = data.split("\n\n")
patterns = patterns_str.split(", ")

designs = []
for design in designs_str.splitlines():
    designs.append(design)

possible = 0
for design in designs:
    stack = [design]
    while stack:
        remaining = stack.pop()
        if len(remaining) == 0:
            possible += 1
            break
        for pattern in patterns:
            if remaining.startswith(pattern):
                stack.append(remaining[len(pattern):])

print(possible)
