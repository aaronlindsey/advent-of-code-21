#!/usr/bin/env python3

SIZE = 5


def find_winner(boards, draws):
    for d in draws:
        for b in boards:

            # blank-out the called number
            for i in range(SIZE):
                for j in range(SIZE):
                    if b[i][j] == d:
                        b[i][j] = ''

            # check for complete row
            for i in range(SIZE):
                streak = 0
                for j in range(SIZE):
                    if b[i][j] == '':
                        streak += 1
                if streak == SIZE:
                    return b, d

            # check for complete column
            for j in range(SIZE):
                streak = 0
                for i in range(SIZE):
                    if b[i][j] == '':
                        streak += 1
                if streak == SIZE:
                    return b, d


boards = []
with open("input") as file:
    lines = file.readlines()
    draws = lines[0].rstrip().split(sep=',')
    board = []
    for line in lines[2:]:
        row = line.rstrip().split()
        if len(row) == 0:
            boards.append(board)
            board = []
        else:
            board.append(row)
    boards.append(board)

winner, called = find_winner(boards, draws)

score = 0
for i in range(SIZE):
    for j in range(SIZE):
        if winner[i][j] != '':
            score += int(winner[i][j])
score *= int(called)

print(score)
