#!/usr/bin/env python3

depth = 0
position = 0
aim = 0
with open("input") as file:
    for line in file:
        parts = line.split()
        command = parts[0]
        value = int(parts[1])
        if command == "forward":
            position += value
            depth += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value

print(position*depth)
