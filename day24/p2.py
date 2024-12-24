from collections import defaultdict
from graphlib import TopologicalSorter

with open("day24/input.txt", "r") as f:
    data = f.read().strip()

wires_str, edges_str = data.split("\n\n")

output_wires = set()
x_wires = set()
y_wires = set()
graph = {}
reversed_graph = defaultdict(set)
gates = {}
for edge_str in edges_str.splitlines():
    inputs, output = edge_str.split(" -> ")
    left, gate, right = inputs.split(" ")
    assert gates.get((left, right, output), gate) == gate
    
    gates[(left, right, output)] = gate
    graph[output] = (left, right)
    
    reversed_graph[left].add(output)
    reversed_graph[right].add(output)

    if left.startswith("z"):
        output_wires.add(left)
    if left.startswith("x"):
        x_wires.add(left)
    if left.startswith("y"):
        y_wires.add(left)

    if right.startswith("z"):
        output_wires.add(right)
    if right.startswith("x"):
        x_wires.add(right)
    if right.startswith("y"):
        y_wires.add(output)

    if output.startswith("z"):
        output_wires.add(output)
    if output.startswith("x"):
        x_wires.add(output)
    if output.startswith("y"):
        y_wires.add(output)

def int_to_bits(value, n_bits) -> str:
    bits = "".join(bin(value)[2:n_bits + 2]).zfill(n_bits)
    assert len(bits) == n_bits
    return bits

def bits_to_int(bits):
    return int(bits, 2)


def bits_to_wires(bits, prefix, n_bits):
    rbits = "".join(reversed(bits))
    return {
        f"{prefix}{str(i).zfill(2)}": int(rbits[i])
        for i in range(n_bits)
    }

def run(x, y, n_bits):
    x_bits = int_to_bits(x, n_bits)
    y_bits = int_to_bits(y, n_bits)
    
    wires = {
        **bits_to_wires(x_bits, "x", n_bits),
        **bits_to_wires(y_bits, "y", n_bits),
    }

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

    actual = ""
    for wire in sorted(output_wires, reverse=True):
        actual += str(wires[wire])

    expected = int_to_bits(x + y, n_bits)
    assert int(expected, 2) == x + y

    diff = sum(a != b for a, b in zip(expected, actual))
    return diff, actual, expected

n_bits = 46

swaps = [
    ("kth", "z12"),
    ("gsd", "z26"),
    ("tbt", "z32"),
    ("vpm", "qnf"),
]
for (aoutput, boutput) in swaps:
    aleft, aright = graph[aoutput]
    bleft, bright = graph[boutput]

    agate = gates.pop((aleft, aright, aoutput))
    bgate = gates.pop((bleft, bright, boutput))

    gates[(aleft, aright, boutput)] = agate
    gates[(bleft, bright, aoutput)] = bgate

    graph[aoutput] = (bleft, bright)
    graph[boutput] = (aleft, aright)

# for i in reversed(range(n_bits)):
#     # 1 + 1
#     a = ["0"] * n_bits
#     a[i] = "1"
#     a = "".join(a)
#     b = ["0"] * n_bits
#     b[i] = "1"
#     b = "".join(b)
#     d, actual, expected = run(bits_to_int(a), bits_to_int(b), n_bits)
#     # print(n_bits - i)
#     if d != 0:
#         print(n_bits - i)

print(",".join(sorted(set([a for a, b in swaps] + [b for a, b in swaps]))))
