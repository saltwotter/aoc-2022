##### DAY 13 #####
from ast import literal_eval

# Input Processing
with open(f"day13/input.txt") as f:
    pairs = [
        [literal_eval(x) for x in pair.splitlines()] for pair in f.read().split("\n\n")
    ]

# Star 2 Input
all_packets = []
for pair in pairs:
    all_packets += pair


def is_right_order(item_l, item_r) -> int:
    if isinstance(item_l, int) and isinstance(item_r, int):
        return item_l - item_r
    if isinstance(item_l, list) and isinstance(item_r, int):
        return is_right_order(item_l, [item_r])
    if isinstance(item_l, int) and isinstance(item_r, list):
        return is_right_order([item_l], item_r)
    if isinstance(item_l, list) and isinstance(item_r, list):
        for left, right in zip(item_l, item_r):
            if diff := is_right_order(left, right):
                return diff
        else:
            return len(item_l) - len(item_r)

    return 0


# Star 1
result = sum(i for i, (l, r) in enumerate(pairs, 1) if is_right_order(l, r) <= 0)

print("Star 1:", result)

# Star 2
two = sum(
    [is_right_order(packet, [[2]]) <= 0 for packet in all_packets + [[2]] + [[6]]]
)
six = sum(
    [is_right_order(packet, [[6]]) <= 0 for packet in all_packets + [[6]] + [[2]]]
)

print("Star 2:", two * six)
