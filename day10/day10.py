##### DAY 10 #####

# Input Processing
with open(f"day10/input.txt") as f:
    instruction_set: list[str] = f.read().splitlines()

# Star 1
cycle = 1
register = 1
cycle_results: dict[int, int] = {}

for instruction in instruction_set:
    if instruction[0] == "n":
        cycle_results[cycle] = register
        cycle += 1
    else:
        modifier = int(instruction.split(" ")[1])
        for _ in range(2):
            cycle_results[cycle] = register
            cycle += 1
        register += modifier

star1 = 0
for pos in [20, 60, 100, 140, 180, 220]:
    star1 += cycle_results[pos] * pos

print("Star 1:", star1)

# Star 2
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


crt = divide_chunks(
    [
        "#"
        if cycle_results[pos] in ((pos % 40) - 2, (pos % 40) - 1, (pos % 40))
        else "."
        for pos in cycle_results.keys()
    ],
    40,
)

print("\n".join(["".join(x) for x in crt]))
