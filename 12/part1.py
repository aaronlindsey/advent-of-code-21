#!/usr/bin/env python3

START = 'start'
END = 'end'


def is_small_cave(v):
    return v != START and v != END and v.islower()


def path_to_string(path):
    return '-'.join(path)


def find_unique_paths(G, v, path=None, visited_small_caves=None):
    if path is None:
        path = []
    if visited_small_caves is None:
        visited_small_caves = []

    path.append(v)
    if is_small_cave(v):
        visited_small_caves.append(v)

    unique_paths = set()
    if v == END:
        unique_paths.add(path_to_string(path))
    else:
        for u in filter(lambda x: x != START and x not in visited_small_caves, G[v]):
            unique_paths |= find_unique_paths(G, u, path, visited_small_caves)

    if is_small_cave(v):
        visited_small_caves.pop()
    path.pop()
    return unique_paths


G = {}
with open("input") as file:
    for line in file:
        parts = line.rstrip().split(sep='-')
        start = parts[0]
        end = parts[1]
        if start not in G:
            G[start] = [end]
        elif end not in G[start]:
            G[start].append(end)
        if end not in G:
            G[end] = [start]
        elif start not in G[end]:
            G[end].append(start)

print(len(find_unique_paths(G, START)))
