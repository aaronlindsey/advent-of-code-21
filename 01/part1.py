#!/usr/bin/env python3

previous = 9000
count = 0

with open("input") as file:
    for line in file:
        current = int(line.rstrip())
        if current > previous:
            count += 1
        previous = current

print(count)
