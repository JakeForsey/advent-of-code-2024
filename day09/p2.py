from typing import NamedTuple, Optional

class Block(NamedTuple):
    size: int
    file_id: Optional[int]

with open("day09/input.txt", "r") as f:
    data = f.read()

blocks = []
for block_id, c in enumerate(data):
    size = int(c)
    if block_id % 2 == 0:
        file_id = block_id // 2
        blocks.append(Block(size, file_id))
    else:
        blocks.append(Block(size, None))

file_id = max(block.file_id for block in blocks if block.file_id is not None)
while file_id > 0:
    file_block = None
    for file_block_index, block in enumerate(blocks):
        if block.file_id is not None and block.file_id == file_id:
            file_block = block
            break

    free_block = None
    for free_block_index, block in enumerate(blocks[:file_block_index]):
        if block.file_id is None and block.size >= file_block.size:
            free_block = block
            assert blocks[free_block_index + 1].file_id is not None, blocks[free_block_index + 1]
            break

    if free_block is None:
        file_id -= 1
        continue

    if free_block.size == file_block.size:
        blocks[free_block_index] = file_block
        blocks[file_block_index] = free_block
    else:
        blocks[free_block_index] = file_block
        blocks.insert(
            free_block_index + 1,
            Block(free_block.size - file_block.size, None),
        )
        blocks[file_block_index + 1] = Block(file_block.size, None)

    file_id -= 1

checksum = 0
position = 0
for block in blocks:
    if block.file_id is None:
        position += block.size
        continue
    for _ in range(block.size):
        checksum += position * block.file_id
        position += 1

print(checksum)
