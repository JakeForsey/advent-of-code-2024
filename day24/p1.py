from graphlib import TopologicalSorter

with open("day24/input.txt", "r") as f:
    data = f.read().strip()

wires_str, edges_str = data.split("\n\n")

wires = {}
for wire_str in wires_str.splitlines():
    wire, value = wire_str.split(": ")
    wires[wire] = int(value)

output_wires = set()
graph = {}
gates = {}
for edge_str in edges_str.splitlines():
    inputs, output = edge_str.split(" -> ")
    left, gate, right = inputs.split(" ")
    gates[(left, right, output)] = gate
    graph[output] = (left, right)
    if left.startswith("z"):
        output_wires.add(left)
    if right.startswith("z"):
        output_wires.add(right)
    if output.startswith("z"):
        output_wires.add(output)

for node in TopologicalSorter(graph).static_order():
    if node in wires:
        value = wires[node]
    else:
        left, right = graph[node]
        gate = gates[(left, right, node)]
        if gate == "AND":
            value = wires[left] & wires[right]
        elif gate == "OR":
            value = wires[left] | wires[right]
        elif gate == "XOR":
            value = wires[left] ^ wires[right]
        else:
            raise AssertionError("Unreachable")
        wires[node] = value

    if all(wire in wires for wire in output_wires):
        break

binary = ""
for wire in sorted(output_wires, reverse=True):
    binary += str(wires[wire])
print(int(binary, 2))
