#!/usr/bin/env python3

MATCHING_CHARS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
OPENING_CHARS = MATCHING_CHARS.keys()
POINTS_PER_CHAR = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def score(line):
    stack = []
    for char in line:
        if char in OPENING_CHARS:
            stack.append(char)
        else:
            expected = stack.pop()
            if char != MATCHING_CHARS[expected]:
                return POINTS_PER_CHAR[char]
    return 0


result = 0
with open("input") as file:
    for line in file:
        result += score(line.rstrip())
print(result)
