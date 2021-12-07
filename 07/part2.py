#!/usr/bin/env python3

from statistics import mean

with open("input") as file:
    positions = [int(i) for i in file.readline().rstrip().split(sep=',')]

avg = int(mean(positions))

fuel = 0
for pos in positions:
    n = abs(avg - pos)
    fuel += int(n * (n + 1) / 2)

print(fuel)
