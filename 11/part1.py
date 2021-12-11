#!/usr/bin/env python3

data = []
with open("input") as file:
    for line in file:
        row = [int(i) for i in line.rstrip()]
        data.append(row)

ROWS = len(data)
COLS = len(data[0])


def increase_energy():
    for i in range(ROWS):
        for j in range(COLS):
            data[i][j] += 1


def scan_flashes():
    count = 0
    for i in range(ROWS):
        for j in range(COLS):
            if data[i][j] > 9:
                flash(i, j)
                count += 1
    return count


def flash(row, col):
    data[row][col] = 0
    for i in range(max(0, row - 1), min(ROWS, row + 2)):
        for j in range(max(0, col - 1), min(COLS, col + 2)):
            if data[i][j] != 0:
                data[i][j] += 1


STEPS = 100

result = 0
for i in range(STEPS):
    increase_energy()
    flashes = scan_flashes()
    while flashes != 0:
        result += flashes
        flashes = scan_flashes()
print(result)
