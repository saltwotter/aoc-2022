##### DAY 12 #####

# Input Processing
from queue import PriorityQueue


with open(f"day12/inputtest.txt") as f:
    heightmap: list[list[str]] = f.read().splitlines()

key: dict[str, int] = {}
[key.update({b: a}) for a, b in enumerate("abcdefghijklmnopqrstuvwxyz")]
key["S"] = 0
key["E"] = 25

# Star 1
def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for row_num, row in enumerate(grid):
        for col_num, col in enumerate(row):
            if col == "S":
                return (row_num, col_num)


def find_end(grid: list[list[str]]) -> tuple[int, int]:
    for row_num, row in enumerate(grid):
        for col_num, col in enumerate(row):
            if col == "E":
                return (row_num, col_num)


def valid_path(grid: list[list[str]], position, new):
    current = grid[position[0]][position[1]]
    new_pos = grid[new[0]][new[1]]
    return key[new_pos] <= key[current] + 1


def distance(a: list[str], b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def traverse(grid: list[list[str]]) -> None:
    lower_bound = len(grid)
    right_bound = len(grid[0])
    end = find_end(grid)
    start = find_start(grid)
    traversing = PriorityQueue()
    costs = {start: 0}
    history = set()
    history.add(start)
    offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))
    traversing.put((0, start))

    while not traversing.empty():
        position = traversing.get()[1]
        if position == end and grid[position[0]][position[1]] == "z":
            break
        for offset in offsets:
            new = (position[0] + offset[0], position[1] + offset[1])
            if (
                0 <= new[0] < lower_bound
                and 0 <= new[1] < right_bound
                and valid_path(grid, position, new)
            ):
                new_cost = costs[position] + 1
                if new not in history or new_cost < costs[new]:
                    costs[new] = new_cost
                    priority = new_cost + distance(new, end)
                    traversing.put((priority, new))
                    history.add(new)
    return costs[position]


print("Star 1:", traverse(grid=heightmap))
