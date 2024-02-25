import math
import sys
from pathlib import Path
from typing import List, Tuple


def parse_input(part: str) -> Tuple[List[int], List[int]]:
    if part == "1":
        filename = "input1.txt"
    elif part == "1s":
        filename = "input1_s.txt"
    elif part == "2":
        filename = "input1.txt"
    else:
        filename = "input1_s.txt"
    with open(Path(__file__).parent / filename, "r") as f:
        lines = f.readlines()

    time = []
    distance = []
    for line in lines:
        line = line.strip().split(" ")
        if "Time:" in line[0]:
            time.extend([l for l in line[1:] if l != ""])
        else:
            distance.extend([l for l in line[1:] if l != ""])
    if "2" in part:
        time = "".join(time)
        distance = "".join(distance)
        time = [int(time)]
        distance = [int(distance)]
    else:
        time = list(map(int, time))
        distance = list(map(int, distance))

    return time, distance


def score_function(button: int, time: int) -> int:
    """
    given how long button held,
    calculate speed and distance over ramaining time
    """
    speed = button
    time -= button
    return speed * time

def main(part: str) -> int:
    """
    this will be solved in 2 steps.
    1. itterate forward until the frist time that a distance is greater than the record.
    2. itterate backwards until the frist time that a distance is greater than the record.
    every point between these two points will also be greater than the record.
    """
    times, distances = parse_input(part)
    answer = []
    for time, distance in zip(times, distances):
        break_points = []
        for t in range(time):
            if score_function(t, time) > distance:
                break_points.append(t)
                break
        for t in range(time, break_points[0], -1):
            if score_function(t, time) > distance:
                break_points.append(t)
                break
        answer.append(break_points[1] - break_points[0] + 1)
    return math.prod(answer)


if __name__ == "__main__":
    part = sys.argv[1]
    print(main(part))
