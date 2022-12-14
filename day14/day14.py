##### DAY 14 #####

# Input Processing
with open(f"day14/input.txt") as f:
    lines = [
        [tuple([int(x) for x in coord.split(",")]) for coord in line.split(" -> ")]
        for line in f.read().splitlines()
    ]


def generate_wall(
    start: tuple[int, int], end: tuple[int, int]
) -> list[tuple[int, int]]:
    result = [start, end]
    if start[0] != end[0]:
        for x in range(*sorted([start[0] + 1, end[0]])):
            result.append((x, start[1]))
    else:
        for y in range(*sorted([start[1] + 1, end[1]])):
            result.append((start[0], y))

    return result


def emit_sand(
    start_x: int,
    start_y: int,
    lower_bound: int,
    walls: set[tuple[int, int]],
    at_rest: set[tuple[int, int]],
) -> tuple[int, int]:
    curr_x = start_x
    curr_y = start_y
    while curr_y < lower_bound:
        if (curr_x, curr_y + 1) not in walls and (
            curr_x,
            curr_y + 1,
        ) not in at_rest:
            curr_y += 1
        elif (curr_x - 1, curr_y + 1) not in walls and (
            curr_x - 1,
            curr_y + 1,
        ) not in at_rest:
            curr_x -= 1
            curr_y += 1
        elif (curr_x + 1, curr_y + 1) not in walls and (
            curr_x + 1,
            curr_y + 1,
        ) not in at_rest:
            curr_x += 1
            curr_y += 1
        else:
            return (curr_x, curr_y)
    return (-1, -1)


def emit_sand_redo(
    start_x: int,
    start_y: int,
    walls: set[tuple[int, int]],
    at_rest: set[tuple[int, int]],
) -> tuple[int, int]:
    curr_x = start_x
    curr_y = start_y
    while (start_x, start_y) not in at_rest:
        if (curr_x, curr_y + 1) not in walls and (
            curr_x,
            curr_y + 1,
        ) not in at_rest:
            curr_y += 1
        elif (curr_x - 1, curr_y + 1) not in walls and (
            curr_x - 1,
            curr_y + 1,
        ) not in at_rest:
            curr_x -= 1
            curr_y += 1
        elif (curr_x + 1, curr_y + 1) not in walls and (
            curr_x + 1,
            curr_y + 1,
        ) not in at_rest:
            curr_x += 1
            curr_y += 1
        else:
            return (curr_x, curr_y)
    return (-1, -1)


walls: list[tuple[int, int]] = []

for line in lines:
    for start, end in zip(line[0 : len(line) - 1], line[1:]):
        walls += generate_wall(start, end)

walls = set(walls)
at_rest: set[tuple[int, int]] = set()
lower_bound = max([x[1] for x in list(walls)])
emitter_x = 500
emitter_y = 0

# Star 1
while (
    sand := emit_sand(
        start_x=emitter_x,
        start_y=emitter_y,
        lower_bound=lower_bound,
        walls=walls,
        at_rest=at_rest,
    )
) != (-1, -1):
    at_rest.add(sand)
print("Star 1:", len(at_rest))

# Star 2
for x in range(-1, 1000):
    walls.add((x, lower_bound + 2))

at_rest: set[tuple[int, int]] = set()

while (
    sand := emit_sand_redo(
        start_x=emitter_x,
        start_y=emitter_y,
        walls=walls,
        at_rest=at_rest,
    )
) != (-1, -1):
    at_rest.add(sand)

print("Star 2:", len(at_rest))
