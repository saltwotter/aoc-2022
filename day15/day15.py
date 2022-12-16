##### DAY 15 #####

# Input Processing
with open(f"day15/input.txt") as f:
    readings = [
        [
            tuple([int(x) for x in pair.split(", y=")])
            for pair in line[12:].split(": closest beacon is at x=")
        ]
        for line in f.read().splitlines()
    ]

# Star 1
def get_manhattan_distance(sensor: tuple[int, int], beacon: tuple[int, int]) -> int:
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


def determine_diamond_area(
    reading: list[tuple[int, int]], distance: int, y_filter: int
) -> list[int]:
    sens_x, sens_y = reading[0]
    if (sens_dist := abs(sens_y - y_filter)) < distance:
        x_dist = distance - sens_dist
        return list(set(range(sens_x - x_dist, sens_x + x_dist)))
    return []


def get_all_diamond_areas(reading: list[tuple[int, int]], y_filter: int) -> int:
    return determine_diamond_area(reading, get_manhattan_distance(*reading), y_filter)


def count_available_in_y(readings: list[list[tuple[int, int]]], y: int) -> int:
    all_diamonds = [get_all_diamond_areas(reading, y) for reading in readings]
    return len(set([inner for outer in all_diamonds for inner in outer]))


print(
    "Star 1:",
    count_available_in_y(readings, y=2000000),
)

# Star 2
import z3

lower_bound = 4_000_000
solver = z3.Solver()
x, y = z3.Int("x"), z3.Int("y")

solver.add(x >= 0)
solver.add(x <= lower_bound)
solver.add(y >= 0)
solver.add(y <= lower_bound)


def z3_abs(x):
    return z3.If(x >= 0, x, -x)


for sensor, beacon in readings:
    dist = get_manhattan_distance(sensor, beacon)
    solver.add(z3_abs(sensor[0] - x) + z3_abs(sensor[1] - y) > dist)

assert solver.check() == z3.sat
model = solver.model()
print("Part 2:", model[x].as_long() * lower_bound + model[y].as_long())

# DOES NOT WORK
# y = mx + b
# m_vars, b_vars = set(), set()
# for reading in readings:
#     x, y = reading[0]
#     radius = get_manhattan_distance(*reading)
#     m_vars.add(y - x + radius + 1)
#     m_vars.add(y - x - radius - 1)
#     b_vars.add(y + x + radius + 1)
#     b_vars.add(y + x - radius - 1)


# for m in m_vars:
#     for b in b_vars:
#         p = ((b - m) // 2, (b - m) // 2)
#         if all(0 < c < lower_bound for c in p) and all(
#             get_manhattan_distance(reading[0], p) > get_manhattan_distance(*reading)
#             for reading in readings
#         ):
#             print(lower_bound * p[0] + p[1])
