#!/usr/bin/env python3

count = 0
with open("input") as file:
    for line in file:
        parts = line.rstrip().split(sep='|')
        output = parts[1].rstrip().split()
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                count += 1

print(count)
