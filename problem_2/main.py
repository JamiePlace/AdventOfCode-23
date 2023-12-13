from pathlib import Path
import math


max_allowable = {"red": 12, "green": 13, "blue": 14}


def read_file():
    path = Path(__file__).parent / "input.txt"
    with open(path, "r") as f:
        lines = f.readlines()
    for line in lines:
        yield line


def part1():
    strings = read_file()
    game_counts = {}
    for i, string in enumerate(strings):
        max_values = {"red": -math.inf, "green": -math.inf, "blue": -math.inf}
        string = string.replace(" ", "")
        game_id, subsets = string.split(":")
        # remove the 'Game' from the string
        game_id = "".join(filter(str.isdigit, game_id))
        subsets = subsets.split(";")
        for subset in subsets:
            n_balls = subset.split(",")
            for ball in n_balls:
                count = "".join(filter(str.isdigit, ball))
                colour = "".join(filter(str.isalpha, ball))
                if int(count) > max_values[colour]:
                    max_values[colour] = int(count)
        game_counts[i + 1] = max_values
        for key, value in max_values.items():
            if value > max_allowable[key]:
                del game_counts[i + 1]
                break
    return sum(game_counts.keys())


def part2():
    strings = read_file()
    game_counts = {}
    game_power = []
    for i, string in enumerate(strings):
        max_values = {"red": -math.inf, "green": -math.inf, "blue": -math.inf}
        string = string.replace(" ", "")
        game_id, subsets = string.split(":")
        # remove the 'Game' from the string
        game_id = "".join(filter(str.isdigit, game_id))
        subsets = subsets.split(";")
        for subset in subsets:
            n_balls = subset.split(",")
            for ball in n_balls:
                count = "".join(filter(str.isdigit, ball))
                colour = "".join(filter(str.isalpha, ball))
                if int(count) > max_values[colour]:
                    max_values[colour] = int(count)
        game_counts[i + 1] = max_values

    for _, value in game_counts.items():
        game_power.append(value["red"] * value["green"] * value["blue"])
    return sum(game_power)


if __name__ in "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())
