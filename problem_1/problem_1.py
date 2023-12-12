import re
from pathlib import Path
import math

valid_keys = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def read_file():
    path = Path(__file__).parent / "strings.txt"
    with open(path, "r") as f:
        lines = f.readlines()
    for line in lines:
        yield line


def find_first_and_last_numbers(string):
    char1, char2 = "", ""
    pos1, pos2 = math.inf, -math.inf
    for key in valid_keys.keys():
        iterator = re.finditer(key, string)
        for match in iterator:
            if match.start() < pos1:
                pos1 = match.start()
                char1 = key

            if match.start() > pos2:
                pos2 = match.start()
                char2 = key

    return int(valid_keys[char1] + valid_keys[char2])


if __name__ in "__main__":
    strings = read_file()
    _sum = 0
    for string in strings:
        digits = find_first_and_last_numbers(string)
        assert digits < 100
        _sum += digits
    print(_sum)
