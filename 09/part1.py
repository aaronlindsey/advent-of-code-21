#!/usr/bin/env python3

data = []
with open("input") as file:
    for line in file:
        r = [int(i) for i in line.rstrip()]
        data.append(r)

ROWS = len(data)
COLUMNS = len(data[0])


def is_low_point(row, col):
    for i in range(max(0, row - 1), min(ROWS, row + 2)):
        for j in range(max(0, col - 1), min(COLUMNS, col + 2)):
            if (row != i or col != j) and data[row][col] >= data[i][j]:
                return False
    return True


result = 0
for row in range(ROWS):
    for col in range(COLUMNS):
        if is_low_point(row, col):
            result += data[row][col] + 1
print(result)
