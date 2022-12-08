##### DAY 7 #####

# Input Processing
with open(f"day7/input.txt") as f:
    input_string: str = [x for x in f.read().split("\n") if x != ""]


class Directory:
    def __init__(self, name: str, parent: "Directory" = None):
        self.name: str = name
        self.parent: Directory = parent
        self.children: dict[str, Directory] = {}
        self.size = 0

    def generate_total_size(self) -> int:
        [child.generate_total_size() for child in list(self.children.values())]
        self.size += sum([child.size for child in list(self.children.values())])

    def add_child(self, dir_name: str) -> None:
        self.children[dir_name] = Directory(name=dir_name, parent=self)

    def add_size(self, file_size: int) -> None:
        self.size += file_size

    def determine_if_big(self) -> list[int]:
        result = []
        for child in self.children.values():
            result += child.determine_if_big()
        return (result + [self.size]) if self.size <= 100_000 else result

    def get_all_sizes(self) -> list[int]:
        # ADDED FOR STAR 2
        result = []
        for child in self.children.values():
            result += child.get_all_sizes()
        return result + [self.size]


def process_output(commands: list[str]):
    base = Directory(name="/")
    current_dir = base
    for command in commands[1:]:
        if command[0] == "d":
            current_dir.add_child(dir_name=command.split(" ")[1])
        elif command[0] in "0123456789":
            current_dir.add_size(int(command.split(" ")[0]))
        elif command[0:4] == "$ cd":
            if command.split(" ")[2] == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.children[command.split(" ")[2]]

    return base


main = process_output(commands=input_string)
main.generate_total_size()

# Star 1
print("Star 1:", sum(main.determine_if_big()))

# Star 2
DISK_SPACE = 70_000_000
NEEDED_SPACE = 30_000_000

all_sizes = main.get_all_sizes()
total_size = main.size
all_sizes.sort()

for size in all_sizes:
    if DISK_SPACE - total_size + size >= NEEDED_SPACE:
        print("Star 2:", size)
        break
