from typing import List

import numpy as np
from rich import print

neighbours = [
    [0, 1],  # right
    [0, -1],  # left
    [-1, 0],  # up
    [1, 0],  # down
]

pipes = {
    "|": [neighbours[2], neighbours[3]],
    "-": [neighbours[0], neighbours[1]],
    "L": [neighbours[2], neighbours[0]],
    "J": [neighbours[2], neighbours[1]],
    "7": [neighbours[3], neighbours[1]],
    "F": [neighbours[3], neighbours[0]],
}


def adjacent_letters(coords: List[int], array: np.ndarray) -> List[str]:
    output = []
    for nc in neighbours:
        # catch boundry conditions
        if coords[0] + nc[0] < 0 or coords[1] + nc[1] < 0:
            continue
        output.append(array[coords[0] + nc[0], coords[1] + nc[1]])
    output = [v for v in output if v != "."]
    return output


def invert_pipes(pipe: List[List[int]]) -> List[int]:
    inv_pipe = []
    for c in pipe:
        inv_pipe.append([-1 * v for v in c])
    return inv_pipe

def is_element(ls1, ls2):
    for ls in ls2:
        if ls1 in ls:
            return True
    return False

def pipe_connections(pipe1: List[List[int]], pipe2: List[List[int]]) -> int:
    count = 0
    for p1 in pipe1:
        if is_element(p1, pipe2):
            count += 1
    return count


with open("input1_s.txt", "r") as file:
    data = file.readlines()

data = np.array([line.strip() for line in data])
# the lenght of each row
rl = len(data[0])
data = np.array(list("".join(data)))
data = data.reshape((len(data) // rl, rl))
row, col = np.where(data == "S")
row, col = row[0], col[0]
nl = adjacent_letters([row, col], data)

nc = [pipes[l] for l in nl]
inverted_pipe = [invert_pipes(p) for p in nc]

connections = {p : pipe_connections(pipes[p], inverted_pipe) for p in pipes.keys()}

print(data)
print(nl)
print([pipes[n] for n in nl])
print(inverted_pipe)
print(connections)

