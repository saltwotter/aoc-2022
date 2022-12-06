##### DAY 6 #####

# Input Processing
with open(f"day6/input.txt") as f:
    input_string: str = f.readlines()[0]

# Star 1
def find_packet_start(datastream: str) -> int:
    buffer = []
    for pos in range(1, len(datastream) + 1):
        if (
            datastream[pos - 1] not in buffer
            and len(buffer) == 3
            and len(set(buffer)) == len(buffer)
        ):
            return pos
        elif len(buffer) == 3:
            buffer.pop(0)
        buffer.append(datastream[pos - 1])


print("Star 1:", find_packet_start(datastream=input_string))

# Star 2
def find_message_start(datastream: str) -> int:
    buffer = []
    for pos in range(1, len(datastream) + 1):
        if (
            datastream[pos - 1] not in buffer
            and len(buffer) == 13
            and len(set(buffer)) == len(buffer)
        ):
            return pos
        elif len(buffer) == 13:
            buffer.pop(0)
        buffer.append(datastream[pos - 1])


print("Star 2:", find_message_start(datastream=input_string))
