#!/usr/bin/env python3

depth = 0
position = 0
with open("input") as file:
    for line in file:
        parts = line.split()
        command = parts[0]
        value = int(parts[1])
        if command == "forward":
            position += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value

print(position*depth)
