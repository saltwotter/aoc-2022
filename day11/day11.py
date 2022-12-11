##### DAY 11 #####
import math as m

# Input Processing
with open(f"day11/input.txt") as f:
    monkey_input: list[list[str]] = [
        monkey.splitlines() for monkey in f.read().split("\n\n")
    ]


class Monkey:
    def __init__(
        self,
        monkey_num: int,
        items: list[int],
        operation: str,
        divisible: int,
        true_monkey: int,
        false_monkey: int,
    ):
        self.monkey_num = monkey_num
        self.items = items
        self.operation = operation
        self.divisible = divisible
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspection_count = 0

    def add_item(self, item: int) -> None:
        self.items.append(item)

    def inspect(self, item: int) -> int:
        self.inspection_count += 1
        oper, num = self.operation[1:].split(" ")
        num = int(num)
        if oper == "*":
            return item * num
        elif oper == "+":
            return item + num
        else:
            return item**num

    def test(self, item: int) -> bool:
        return item % self.divisible == 0

    def turn(self, monkeys: dict[int, "Monkey"], modulo: int) -> None:
        if not self.items:
            return
        while self.items:
            # item = int(self.inspect(self.items.pop(0)) / 3)
            item = self.inspect(self.items.pop(0) % modulo)
            to_monkey = self.true_monkey if self.test(item=item) else self.false_monkey
            monkeys[to_monkey].add_item(item=item)

    def get_inspection_count(self) -> str:
        return f"Monkey {self.monkey_num} inspected {self.inspection_count} times."

    def __str__(self):
        return f"Monkey {self.monkey_num}: {self.items}"


def create_monkey(monkey_input: list[str]) -> Monkey:
    monkey_num = int(monkey_input[0][7])
    items = [int(x) for x in monkey_input[1][18:].split(", ")]
    operation = " ** 2" if monkey_input[2][22:] == " * old" else monkey_input[2][22:]
    divisible = int(monkey_input[3][21:])
    true_monkey = int(monkey_input[4][29:])
    false_monkey = int(monkey_input[5][30:])

    return {
        monkey_num: Monkey(
            monkey_num=monkey_num,
            items=items,
            operation=operation,
            divisible=divisible,
            true_monkey=true_monkey,
            false_monkey=false_monkey,
        )
    }


monkeys: dict[int, Monkey] = {}
for monkey in monkey_input:
    monkeys.update(create_monkey(monkey_input=monkey))

# Star 1
# iters = 20

# for _ in range(iters):
#     for monkey in monkeys.keys():
#         monkeys[monkey].turn(monkeys=monkeys)

# star1 = sorted([monkey.inspection_count for monkey in monkeys.values()], reverse=True)
# print("Star 1:", star1[0] * star1[1])

# Star 2
iters = 10000
modulo = m.prod([monkey.divisible for monkey in monkeys.values()])

for _ in range(iters):
    for monkey in monkeys.keys():
        monkeys[monkey].turn(monkeys=monkeys, modulo=modulo)

star1 = sorted([monkey.inspection_count for monkey in monkeys.values()], reverse=True)
print("Star 2:", star1[0] * star1[1])
