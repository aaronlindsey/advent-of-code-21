#!/usr/bin/env python3

depths = []
with open("input") as file:
    for line in file:
        depths.append(int(line.rstrip()))

count, prev = 0, 0
for i in range(2, len(depths)):
    curr = depths[i] + depths[i-1] + depths[i-2]
    if i > 2 and curr > prev:
        count += 1
    prev = curr

print(count)
