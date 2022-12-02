##### DAY 2 #####

# Input Processing
with open(f"day2/input.txt") as f:
    pairs = [x.split(" ") for x in f.read().splitlines()]

# Star 1
choice_score = {"X": 1, "Y": 2, "Z": 3}


def game_outcome(pair: list[str]) -> int:
    if pair in (["C", "X"], ["A", "Y"], ["B", "Z"]):
        return 6
    elif pair in (["A", "X"], ["B", "Y"], ["C", "Z"]):
        return 3
    else:
        return 0


print("Star 1:", sum([game_outcome(x) + choice_score[x[1]] for x in pairs]))

# Star 2
win_score = {"A": 2, "B": 3, "C": 1}
draw_score = {"A": 1, "B": 2, "C": 3}
lose_score = {"A": 3, "B": 1, "C": 2}


def scorer(pair: list[str]) -> int:
    opp_choice, need = pair
    if need == "X":
        return 0 + lose_score[opp_choice]
    elif need == "Y":
        return 3 + draw_score[opp_choice]
    else:
        return 6 + win_score[opp_choice]


print("Star 2:", sum([scorer(x) for x in pairs]))
