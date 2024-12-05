from collections import defaultdict

with open("day05/input.txt", "r") as f:
    data = f.read()

rules = defaultdict(set)
updates = set()
parsing_rules = True
for line in data.splitlines():
    if line.strip() == "":
        parsing_rules = False
        continue
    
    if parsing_rules:
        a, b = map(int, line.split("|"))
        rules[b].add(a)
    else:
        updates.add(tuple(map(int, line.split(","))))

def valid_update(update, rules):
    for i in range(len(update)):
        left = update[i]
        for j in range(i, len(update)):
            right = update[j]
            if right in rules[left]:
                return False
    return True

total = 0
for update in updates:
    if valid_update(update, rules):
        total += update[len(update) // 2]

print(total)