with open("day09/input.txt", "r") as f:
    data = f.read()

memory = []
for i, c in enumerate(data):
    block_size = int(c)
    if i % 2 == 0:
        file_id = i // 2
        for _ in range(block_size):
            memory.append(str(file_id))
    else:
        for _ in range(block_size):
            memory.append(".")

pointer = len(memory) - 1
free = -1
while pointer >= free:
    if memory[pointer] == ".":
        pointer -= 1
        continue
    
    free = memory.index(".")
    if free > pointer:
        break

    memory[free] = memory[pointer]
    memory[pointer] = "."

    pointer -= 1

checksum = 0
for i, c in enumerate(memory):
    if c == ".":
        break
    checksum += i * int(c)

print(checksum)