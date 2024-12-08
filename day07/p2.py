from operator import __add__, __mul__

with open("day07/input.txt", "r") as f:
    data = f.read()

def cat(current, value):
    s_target = str(current)
    s_value = str(value)
    valid = s_target.endswith(s_value)
    try:
        value = int(s_target[:-len(s_value)])
    except:
        value = 0
    return valid, value

def add(current, value):
    result = current - value
    return result >= 0, result

def mul(current, value):
    return current % value == 0, current // value

result = 0
for line in data.splitlines():
    target, elements = line.split(": ")
    target = int(target)
    elements = list(map(int, elements.split()))

    stack = [(target, len(elements) - 1)]
    while stack:
        value, index = stack.pop()

        if index == -1:
            if 0 == value:
                result += target
                break
            else:
                continue
        
        for op in [cat, mul, add]:
            valid, next_value = op(value, elements[index])
            if not valid:
                continue
            stack.append((next_value, index - 1))

print(result)
