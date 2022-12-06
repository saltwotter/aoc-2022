##### DAY 4 #####

# Input Processing
with open(f"day4/input.txt") as f:
    split_sacks = [
        [[int(x) for x in section.split("-")] for section in pair.split(",")]
        for pair in f.read().splitlines()
    ]

# Star 1
def test_superset(pair: list[list[int, int]]) -> bool:
    set1 = set(range(pair[0][0], pair[0][1] + 1))
    set2 = set(range(pair[1][0], pair[1][1] + 1))
    return set1.issuperset(set2) or set2.issuperset(set1)


results = [test_superset(pair=pair) for pair in split_sacks]
print("Star 1:", sum(results))

# Star 2
def test_intersection(pair: list[list[int, int]]) -> bool:
    set1 = set(range(pair[0][0], pair[0][1] + 1))
    set2 = set(range(pair[1][0], pair[1][1] + 1))
    return not set1.isdisjoint(set2) or not set2.isdisjoint(set1)


results = [test_intersection(pair=pair) for pair in split_sacks]
print("Star 2:", sum(results))
