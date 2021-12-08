#!/usr/bin/env python3

signals = []
outputs = []
with open("input") as file:
    for line in file:
        parts = line.rstrip().split(sep='|')

        # sort the characters for each pattern so they're easier to compare
        signal = [''.join(sorted(x)) for x in parts[0].rstrip().split()]
        signals.append(signal)

        output = [''.join(sorted(x)) for x in parts[1].rstrip().split()]
        outputs.append(output)

result = 0
for i, signal in enumerate(signals):
    value_for_pattern = {}
    p1 = ''
    p4 = ''

    # find patterns 1, 4, 7, and 8
    for pattern in signal:
        if len(pattern) == 2:
            value_for_pattern[pattern] = 1
            p1 = pattern
        elif len(pattern) == 4:
            value_for_pattern[pattern] = 4
            p4 = pattern
        elif len(pattern) == 3:
            value_for_pattern[pattern] = 7
        elif len(pattern) == 7:
            value_for_pattern[pattern] = 8

    # find patterns 2, 3, and 5
    for pattern in signal:
        if len(pattern) == 5:
            if len(set(pattern) & set(p1)) == 2:
                value_for_pattern[pattern] = 3
            elif len(set(pattern) & set(p4)) == 2:
                value_for_pattern[pattern] = 2
            else:
                value_for_pattern[pattern] = 5

    # find patterns 0, 6, and 8
    for pattern in signal:
        if len(pattern) == 6:
            if len(set(pattern) & set(p1)) == 1:
                value_for_pattern[pattern] = 6
            elif len(set(pattern) & set(p4)) == 4:
                value_for_pattern[pattern] = 9
            else:
                value_for_pattern[pattern] = 0

    number = ''
    for pattern in outputs[i]:
        number += str(value_for_pattern[pattern])
    result += int(number)

print(result)
