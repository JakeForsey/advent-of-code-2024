with open("day17/input.txt", "r") as f:
    data = f.read()

_, program_str = data.split("\n\n")
program = program_str.split(": ")[1]
program = list(map(int, program.split(",")))

operands = {
    0: lambda a, b, c: 0,
    1: lambda a, b, c: 1,
    2: lambda a, b, c: 2,
    3: lambda a, b, c: 3,
    4: lambda a, b, c: a,
    5: lambda a, b, c: b,
    6: lambda a, b, c: c,
    7: lambda a, b, c: None,
}

def adv(pointer, a, b, c, operand, literal_operand):
    a = a // (2 ** operand)
    return pointer + 2, a, b, c, []

def bxl(pointer, a, b, c, operand, literal_operand):
    b = b ^ literal_operand
    return pointer + 2, a, b, c, []

def bst(pointer, a, b, c, operand, literal_operand):
    b = operand % 8
    return pointer + 2, a, b, c, []

def jnz(pointer, a, b, c, operand, literal_operand):
    if a == 0:
        return pointer + 2, a, b, c, []
    return literal_operand, a, b, c, []

def bxc(pointer, a, b, c, operand, literal_operand):
    b = b ^ c
    return pointer + 2, a, b, c, []

def out(pointer, a, b, c, operand, literal_operand):
    return pointer + 2, a, b, c, [operand % 8]

def bdv(pointer, a, b, c, operand, literal_operand):
    a = a // (2 ** operand)
    return pointer + 2, a, b, c, []

def cdv(pointer, a, b, c, operand, literal_operand):
    c = a // (2 ** operand)
    return pointer + 2, a, b, c, []

operators = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

def run(i):
    a = i
    b = 0
    c = 0
    outputs = []
    ptr = 0
    while ptr < len(program):
        operator = operators[program[ptr]]
        literal_operand = program[ptr + 1]
        operand = operands[literal_operand](a, b, c)
        ptr, a, b, c, o = operator(
            ptr, a, b, c,
            operand,
            literal_operand,
        )
        outputs.extend(o)
    return outputs


min_a = float("inf")
stack = [(0, -1)]
while stack:
    a, i = stack.pop()
    for j in range(8):
        candidate_a = 8 * a + j
        candidate_program = run(candidate_a)
        if candidate_program == program:
            if candidate_a < min_a:
                min_a = candidate_a
            break
        if candidate_program[i] == program[i]:
            stack.append((candidate_a, i - 1))

print(min_a)
