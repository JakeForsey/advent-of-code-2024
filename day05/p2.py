from collections import defaultdict
from functools import cmp_to_key

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

class Comparator:
    def __init__(self, rules):
        self.rules = rules
    
    def __call__(self, a, b):
        if a == b:
            return 0
        if b in self.rules[a]:
            return -1
        if a in self.rules[b]:
            return 1
        raise AssertionError("Shouldnt get here!")

def fix_and_get_middle(update, rules):
    fixed_update = sorted(update, key=cmp_to_key(Comparator(rules)))
    return fixed_update[len(fixed_update) // 2]

total = 0
for update in updates:
    if not valid_update(update, rules):
        total += fix_and_get_middle(update, rules)

print(total)