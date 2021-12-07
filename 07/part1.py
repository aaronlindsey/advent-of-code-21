#!/usr/bin/env python3

from statistics import median

with open("input") as file:
    positions = [int(i) for i in file.readline().rstrip().split(sep=',')]

med = int(median(positions))

fuel = 0
for pos in positions:
    fuel += abs(med - pos)

print(fuel)
