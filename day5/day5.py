##### DAY 5 #####
import queue as q
import re

# Input Processing
def create_lifo_queue(stacks: str) -> dict[int, q.LifoQueue[str]]:
    queues = {}
    num_of_queues = max([int(x) for x in re.findall("\d", stacks[0])])
    for i in range(1, num_of_queues + 1):
        queues[i] = q.LifoQueue()

    for line in stacks:
        for queue, pos in enumerate(range(1, len(line), 4)):
            if line[pos] != " " and line[pos] not in "0123456789":
                queues[queue + 1].put(line[pos])

    return queues


def read_instructions(instructions: list[str]) -> list[list[int, int, int]]:
    return [
        [int(x) for x in re.findall("\d+", step)] for step in instructions if step != ""
    ]


with open(f"day5/input.txt") as f:
    stacks, lines = [part.split("\n") for part in f.read().split("\n\n")]

stacks.reverse()
queues1 = create_lifo_queue(stacks)
queues2 = create_lifo_queue(stacks)
instructions1 = read_instructions(lines)
instructions2 = read_instructions(lines)

# Star 1
def execute_movement1(
    instruction: list[int, int, int], queues: dict[int, q.LifoQueue[str]]
) -> dict[int, q.LifoQueue[str]]:
    num_moves, prequeue, postqueue = instruction
    for _ in range(num_moves):
        queues[postqueue].put(queues[prequeue].get())
    return queues


def get_message(queues: dict[int, q.LifoQueue[str]]) -> str:
    result = ""
    for queue in queues.keys():
        result += queues[queue].get()
    return result


while instructions1:
    queues1 = execute_movement1(instructions1.pop(0), queues1)

print("Star 1:", get_message(queues1))

# Star 2
def execute_movement2(
    instruction: list[int, int, int], queues: dict[int, q.LifoQueue[str]]
) -> dict[int, q.LifoQueue[str]]:
    num_moves, prequeue, postqueue = instruction
    temp_queue = q.LifoQueue()

    for _ in range(num_moves):
        temp_queue.put(queues[prequeue].get())

    for _ in range(num_moves):
        queues[postqueue].put(temp_queue.get())

    return queues


while instructions2:
    queues2 = execute_movement2(instructions2.pop(0), queues2)

print("Star 2:", get_message(queues2))
