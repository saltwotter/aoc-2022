##### DAY 13 #####

# Input Processing
with open(f"day13/inputtest.txt") as f:
    pairs = [[eval(x) for x in pair.splitlines()] for pair in f.read().split("\n\n")]


def is_right_order(pair: list) -> bool:
    val1, val2 = pair
