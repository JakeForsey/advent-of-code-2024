with open("day17/input.txt", "r") as f:
    data = f.read()

registers_str, program_str = data.split("\n\n")

registers = {}
for register_str in registers_str.splitlines():
    register_id, value = register_str.split(": ")
    register_id = register_id.split(" ")[1]
    value = int(value)
    registers[register_id] = value

program = program_str.split(": ")[1]
program = list(map(int, program.split(",")))

operands = {
    0: lambda registers: 0,
    1: lambda registers: 1,
    2: lambda registers: 2,
    3: lambda registers: 3,
    4: lambda registers: registers["A"],
    5: lambda registers: registers["B"],
    6: lambda registers: registers["C"],
    7: lambda registers: None,
}
def adv(pointer, registers, operand, literal_operand):
    registers["A"] = registers["A"] // (2 ** operand)
    return pointer + 2, registers

def bxl(pointer, registers, operand, literal_operand):
    registers["B"] = registers["B"] ^ literal_operand
    return pointer + 2, registers

def bst(pointer, registers, operand, literal_operand):
    registers["B"] = operand % 8
    return pointer + 2, registers

def jnz(pointer, registers, operand, literal_operand):
    if registers["A"] == 0:
        return pointer + 2, registers
    return literal_operand, registers

def bxc(pointer, registers, operand, literal_operand):
    registers["B"] = registers["B"] ^ registers["C"]
    return pointer + 2, registers

def out(pointer, registers, operand, literal_operand):
    print(operand % 8, end=",")
    return pointer + 2, registers

def bdv(pointer, registers, operand, literal_operand):
    registers["B"] = registers["A"] // (2 ** operand)
    return pointer + 2, registers

def cdv(pointer, registers, operand, literal_operand):
    registers["C"] = registers["A"] // (2 ** operand)
    return pointer + 2, registers

operators = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}

def run(registers, program):
    pointer = 0
    while pointer < len(program):
        operator = operators[program[pointer]]
        literal_operand = program[pointer + 1]
        operand = operands[literal_operand](registers)
        pointer, registers = operator(pointer, registers, operand, literal_operand)

    return registers

print(registers)
print(program)
run(registers, program)