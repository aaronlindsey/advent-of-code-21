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


step = 0
while True:
    step += 1

    increase_energy()

    flashes_per_step = 0
    flashes_per_scan = scan_flashes()
    while flashes_per_scan != 0:
        flashes_per_step += flashes_per_scan
        flashes_per_scan = scan_flashes()

    if flashes_per_step == ROWS * COLS:
        break

print(step)
