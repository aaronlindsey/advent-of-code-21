#!/usr/bin/env python3

coords = []
folds = []
with open("input") as file:
    for line in file:
        if line.startswith("fold"):
            parts = line.rstrip().split(sep='=')
            axis = parts[0][-1]  # the character immediately before the '='
            position = int(parts[1])
            folds.append((axis, position))
        else:
            parts = line.rstrip().split(sep=',')
            if len(parts) == 2:
                x = int(parts[0])
                y = int(parts[1])
                coords.append((x, y))

for (axis, position) in folds[:1]:
    new_coords = set(coords)
    for (x, y) in coords:
        if axis == 'x' and position < x:
            dist = x - position
            new_coords.remove((x, y))
            new_coords.add((position - dist, y))
        if axis == 'y' and position < y:
            dist = y - position
            new_coords.remove((x, y))
            new_coords.add((x, position - dist))
    coords = list(new_coords)

print(len(coords))
