#!/usr/bin/env python3

DAYS = 256

with open("input") as file:
    initial_state = [int(i) for i in file.readline().rstrip().split(sep=',')]

fish_per_timer = [0] * 9
for timer in initial_state:
    fish_per_timer[timer] += 1

for i in range(DAYS):
    spawning = fish_per_timer[0]
    for j in range(1, len(fish_per_timer)):
        fish_per_timer[j - 1] = fish_per_timer[j]
    fish_per_timer[6] += spawning
    fish_per_timer[8] = spawning

print(sum(fish_per_timer))
