from pathlib import Path


def read_file():
    path = Path(__file__).parent / "input2.txt"
    with open(path, "r") as f:
        file = f.read().strip().split("\n")
    return file


print(read_file())
