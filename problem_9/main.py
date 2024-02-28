from pathlib import Path
from typing import List
from rich import print

import numpy as np

part = "1"

def parse_input(part: str) -> List[List[int]]:
    if part == "1":
        filename = "input1.txt"
    elif part == "1s":
        filename = "input1_s.txt"
    elif part == "2":
        filename = "input1.txt"
    else:
        filename = "input2_s.txt"
    with open(Path(__file__).parent / filename, "r") as f:
        lines = f.readlines()
    lines = [list(map(int, line.split(" "))) for line in lines]
    return lines

def part1() -> int:
    data = parse_input(part)
    new_number_sum = 0
    for line in data:
        while any([ val != 0 for val in line ]):
            new_number_sum += line[-1]
            line = np.diff(line)
    return new_number_sum

def part2() -> int:
    data = parse_input(part)
    new_number_sum = 0
    count = 0
    for line in data:
        while any([ val != 0 for val in line ]):
            if count % 2 == 0:
                new_number_sum += line[0]
            else:
                new_number_sum -= line[0]
            line = np.diff(line)
            count += 1
        count = 0
    return new_number_sum



if __name__ == "__main__":
    print(part1())
    print(part2())
    pass
