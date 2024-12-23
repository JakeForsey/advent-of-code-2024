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

triples = set()
for node in nodes:
    for other0 in edges[node]:
        for other1 in edges[other0]:
            if node in edges[other1]:
                triples.add(tuple(sorted([node, other0, other1])))

total = 0
for triple in triples:
    if any(n.startswith("t") for n in triple):
        total += 1

print(total)
