##### DAY 1 #####

# Star 1
with open(f"day1/input.txt") as f:
    text = f.read()

elves = [sum([int(x) for x in c.split("\n") if x != ""]) for c in text.split("\n\n")]

print("Part 1:", max(elves))

# Star 2

elves.sort(reverse=True)
print("Part 2:", sum(elves[0:3]))
