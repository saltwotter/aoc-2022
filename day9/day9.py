##### DAY 9 #####

# Input Processing
with open(f"day9/input.txt") as f:
    input_steps: list[tuple[str, int]] = [
        (row.split(" ")[0], int(row.split(" ")[1])) for row in f.read().splitlines()
    ]


class RopeNode:
    def __init__(self, prev_segment: "RopeNode" = None):
        self.visited: set[str] = set()
        self.visited.add("0,0")
        self.curr_pos: list[int, int] = [0, 0]
        self.prev_pos: list[int, int] = [0, 0]
        self.prev_segment: RopeNode = prev_segment
        self.next_segment: RopeNode = None
        if prev_segment:
            prev_segment.next_segment = self

    def add_current_pos_to_visited(self) -> None:
        self.visited.add(",".join([str(x) for x in self.curr_pos]))

    def next_node_not_near(self) -> bool:
        # Return true if the distance for either direction is more than 1
        return (
            abs(self.curr_pos[0] - self.next_segment.curr_pos[0]) > 1
            or abs(self.curr_pos[1] - self.next_segment.curr_pos[1]) > 1
        )

    def check_and_update_next_node(self) -> None:
        # If there is a next segment and it is not near this node,
        # update that node to my last position and have it check its next node.
        if self.next_segment and self.next_node_not_near():
            self.next_segment.follow()

    def move(self, direction: str, times: int) -> None:
        commands = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
        for _ in range(times):
            self.add_current_pos_to_visited()
            self.prev_pos = self.curr_pos
            self.curr_pos = [
                self.curr_pos[0] + commands[direction][0],
                self.curr_pos[1] + commands[direction][1],
            ]
            self.check_and_update_next_node()

    def follow(self) -> None:
        self.add_current_pos_to_visited()
        self.prev_pos = self.curr_pos
        x_delta = self.prev_segment.curr_pos[0] - self.curr_pos[0]
        y_delta = self.prev_segment.curr_pos[1] - self.curr_pos[1]
        x_dir = (1 if x_delta > 0 else -1) if x_delta else 0
        y_dir = (1 if y_delta > 0 else -1) if y_delta else 0
        self.curr_pos = [
            self.curr_pos[0] + x_dir,
            self.curr_pos[1] + y_dir,
        ]
        self.check_and_update_next_node()

    def get_total_visited_squares(self) -> int:
        return len(self.visited)

    def get_last_node_visited(self) -> int:
        # If there is a next segment, do this check there.
        # If there isn't a next segment, return its current node's visited number.
        return (
            self.next_segment.get_last_node_visited()
            if self.next_segment
            else self.get_total_visited_squares()
        )


# Star 1
head = RopeNode()
tail = RopeNode(prev_segment=head)

for step in input_steps:
    head.move(*step)

print("Star 1:", head.get_last_node_visited() + 1)

# Star 2
head = RopeNode()
curr = head
for _ in range(9):
    node = RopeNode(prev_segment=curr)
    curr = node

for step in input_steps:
    head.move(*step)

print("Star 2:", head.get_last_node_visited())
