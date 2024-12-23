from collections import defaultdict

with open("day23/input.txt", "r") as f:
    data = f.read()

edges = defaultdict(set)
nodes = set()
for line in data.splitlines():
    left, right = line.split("-")
    nodes.add(left)
    nodes.add(right)
    edges[left].add(right)
    edges[right].add(left)

max_size = 0
best_password = None
seen = set()
for i, node in enumerate(nodes):

    stack = [{node}]
    while stack:
        component = stack.pop()
        password = ','.join(sorted(component))

        if password in seen:
            continue
        seen.add(password)

        candidates = set()
        for node in component:
            for candidate in edges[node]:
                if candidate in component:
                    continue
                if component.issubset(edges[candidate]):
                    candidates.add(candidate)
        
        if not candidates:
            if len(component) > max_size:
                print(f"new largest component: {max_size} -> {len(component)} {password}")
                max_size = len(component)
                best_password = password
        
        for candidate in candidates:
            stack.append(component | {candidate})

print(best_password)
