#!/usr/bin/env python3

SIZE = 5


def find_last_winner(boards, draws):
    won = [False] * len(boards)

    for d in draws:
        for board_id, b in enumerate(boards):

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
                    won[board_id] = True

            # check for complete column
            for j in range(SIZE):
                streak = 0
                for i in range(SIZE):
                    if b[i][j] == '':
                        streak += 1
                if streak == SIZE:
                    won[board_id] = True

            winners = 0
            for i in range(len(boards)):
                if won[i]:
                    winners += 1
            if winners == len(boards):
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

last_winner, called = find_last_winner(boards, draws)

score = 0
for i in range(SIZE):
    for j in range(SIZE):
        if last_winner[i][j] != '':
            score += int(last_winner[i][j])
score *= int(called)

print(score)
