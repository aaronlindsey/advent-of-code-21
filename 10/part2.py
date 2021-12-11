#!/usr/bin/env python3

MATCHING_CHARS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
OPENING_CHARS = MATCHING_CHARS.keys()
POINTS_PER_CHAR = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def score(line):
    stack = []
    for char in line:
        if char in OPENING_CHARS:
            stack.append(char)
        else:
            expected = stack.pop()
            if char != MATCHING_CHARS[expected]:
                return 0  # for this round we do not score corrupted lines
    result = 0
    for char in reversed(stack):
        result *= 5
        result += POINTS_PER_CHAR[MATCHING_CHARS[char]]
    return result


scores = []
with open("input") as file:
    for line in file:
        s = score(line.rstrip())
        if s != 0:
            scores.append(s)
scores = sorted(scores, reverse=True)
print(scores[len(scores) // 2])
