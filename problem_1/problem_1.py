import re
from pathlib import Path
import numpy as np


def read_file():
    path = Path(__file__).parent / "strings.txt"
    with open(path, "r") as f:
        lines = f.readlines()
    for line in lines:
        yield line


def find_first_and_last_numbers(string):
    # match the first numeric character and last numeric character
    # note: returns nothing if only one numeric character is found:w
    numbers = re.findall(r"^[^\d]*(\d).*(\d)(?!.*\d)", string)
    # if no match is found there is only one numeric character
    # find the "first" numeric character and return it twice
    if len(numbers) == 0:
        numbers = re.findall(r"^[^\d]*(\d)", string)
        cat_string = numbers[0] + numbers[0]
        return int(cat_string)
    cat_string = numbers[0][0] + numbers[0][1]
    return int(cat_string)


if __name__ in "__main__":
    strings = read_file()
    _sum = 0
    for string in strings:
        digits = find_first_and_last_numbers(string)
        assert digits < 100
        _sum += digits
    print(_sum)
