#!/usr/bin/env python3

digits = 12
stuff = [0] * digits
lines = 0
with open("input") as file:
    for line in file:
        lines += 1
        for i in range(digits):
            stuff[i] += int(line[i])

gamma = 0
epsilon = 0
for i in range(digits):
    if stuff[i] > lines/2:
        gamma += 2**(11-i)
    elif stuff[i] < lines/2:
        epsilon += 2**(11-i)

print(gamma*epsilon)
