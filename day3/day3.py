##### DAY 3 #####

# Input Processing
def split_compartments(sack: str) -> list[str]:
    comp_size = int(len(sack) / 2)
    return sack[:comp_size], sack[comp_size:]


with open(f"day3/input.txt") as f:
    split_sacks = [split_compartments(x) for x in f.read().splitlines()]

# Star 1
def get_alpha_position(char: str) -> int:
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) + 1


def find_intersection(sack: tuple[str, str]) -> str:
    return set(sack[0]).intersection(set(sack[1])).pop()


result = [get_alpha_position(find_intersection(x)) for x in split_sacks]
print("Star 1:", sum(result))

# Star 2
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


def find_triple_intersection(sacks: list[str, str, str]) -> str:
    return set(sacks[0]).intersection(set(sacks[1]).intersection(set(sacks[2]))).pop()


sacks = ["".join(x) for x in split_sacks]
groups = list(divide_chunks(sacks, 3))
result = [get_alpha_position(find_triple_intersection(x)) for x in groups]
print("Star 2:", sum(result))
