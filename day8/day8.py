##### DAY 8 #####

# Input Processing
with open(f"day8/input.txt") as f:
    input_grid: list[list[int]] = [
        [int(x) for x in row] for row in f.read().splitlines()
    ]


# Star 1
def get_all_values(grid: list[list[int]], x_cord, y_cord) -> list[list[int]]:
    result = []
    result.append([x[y_cord] for x in grid[:x_cord]][::-1])
    result.append([x[y_cord] for x in grid[x_cord + 1 :]])
    result.append(grid[x_cord][:y_cord][::-1])
    result.append(grid[x_cord][y_cord + 1 :])
    return result


def determine_visible(grid: list[list[int]], x_cord, y_cord) -> bool:
    if x_cord == 0 or y_cord == 0:
        return True
    else:
        to_check = grid[x_cord][y_cord]
        values = get_all_values(grid=grid, x_cord=x_cord, y_cord=y_cord)
        for direction in values:
            if all(item < to_check for item in direction):
                return True
            continue
        return False


star1 = 0
for x in range(len(input_grid)):
    for y in range(len(input_grid[0])):
        star1 += 1 if determine_visible(grid=input_grid, x_cord=x, y_cord=y) else 0

print("Star 1:", star1)

# Star 2
def determine_score(grid: list[list[int]], x_cord, y_cord) -> int:
    if x_cord == 0 or y_cord == 0:
        return 0
    else:
        to_check = grid[x_cord][y_cord]
        left, right, up, down = [
            count_to_block(dir, to_check)
            for dir in get_all_values(grid=grid, x_cord=x_cord, y_cord=y_cord)
        ]
        return left * right * up * down


def count_to_block(los: list[int], tree_height: int) -> int:
    result = 0
    for tree in los:
        result += 1
        if tree >= tree_height:
            return result
    return result


star2_max = 0
for x in range(len(input_grid)):
    for y in range(len(input_grid[0])):
        score = determine_score(grid=input_grid, x_cord=x, y_cord=y)
        star2_max = score if score > star2_max else star2_max

print("Star 2:", star2_max)
