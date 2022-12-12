##### DAY 12 #####
import networkx as nx

# Input Processing
with open(f"day12/input.txt") as f:
    heightmap = {
        (x, y): c
        for y, ln in enumerate(f.read().splitlines())
        for x, c in enumerate(ln)
    }

for pos, value in heightmap.items():
    if value == "S":
        start = pos
        heightmap[pos] = "a"
    if value == "E":
        end = pos
        heightmap[pos] = "z"

# Star 1
OFFSETS = ((0, 1), (1, 0), (0, -1), (-1, 0))
grid = nx.DiGraph()

for pos, value in heightmap.items():
    for x, y in OFFSETS:
        new = (pos[0] + x, pos[1] + y)
        if ord(heightmap.get(new, "Ƥ")) <= ord(value) + 1:  # Blaze it
            grid.add_edge(pos, new)

shortest = len(nx.shortest_path(grid, start, end)) - 1

print("Star 1:", shortest)

# Star 2
all_paths = [
    length
    for pos, length in nx.single_target_shortest_path_length(grid, end, shortest)
    if heightmap[pos] == "a"
]

print("Star 2:", min(all_paths))
