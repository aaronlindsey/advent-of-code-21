#!/usr/bin/env python3

data = []
with open("input") as file:
    for line in file:
        r = [int(i) for i in line.rstrip()]
        data.append(r)

ROWS = len(data)
COLUMNS = len(data[0])


def neighbors_of(row, col):
    for i in range(max(0, row - 1), min(ROWS, row + 2)):
        for j in range(max(0, col - 1), min(COLUMNS, col + 2)):
            if row == i and col == j:
                continue  # the input point is not a neighbor of itself
            if row != i and col != j:
                continue  # diagonal locations are not neighbors
            yield i, j


def is_low_point(row, col):
    for (i, j) in neighbors_of(row, col):
        if data[row][col] >= data[i][j]:
            return False
    return True


def print_visited(visited):
    print()
    for i in range(ROWS):
        for j in range(COLUMNS):
            if (i, j) in visited:
                print(data[i][j], end='')
            else:
                print(' ', end='')
        print()


basins = {}
for row in range(ROWS):
    for col in range(COLUMNS):
        if is_low_point(row, col):
            basins[(row, col)] = None

for low_point in basins:
    to_explore = {low_point}
    visited = set()
    while len(to_explore) != 0:
        point = to_explore.pop()
        visited.add(point)
        row = point[0]
        col = point[1]
        for neighbor in neighbors_of(row, col):
            i = neighbor[0]
            j = neighbor[1]
            if data[i][j] < 9 and neighbor not in visited:
                to_explore.add(neighbor)
    # print_visited(visited)
    basins[low_point] = len(visited)

basin_sizes = sorted(basins.values(), reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
