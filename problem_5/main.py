from pathlib import Path


def read_file():
    path = Path(__file__).parent / "input2.txt"
    with open(path, "r") as f:
        file = f.read().strip().split("\n")
    return file


def parse_file(file):
    output = {}
    for i, line in enumerate(file):
        if i == 0:
            key = line.split(":")[0]
            values = line.split(":")[1].strip().split(" ")
            output[key] = values
    print(output)


print(parse_file(read_file()))
