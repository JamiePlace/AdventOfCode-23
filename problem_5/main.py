import sys
from pathlib import Path
from rich import print


def read_file():
    path = Path(__file__).parent / f"{sys.argv[1]}.txt"
    with open(path, "r") as f:
        file = f.read().strip()
    return file


def parse_file(file):
    output = {}
    key = ""
    for i, line in enumerate(file.split("\n")):
        if i == 0:
            output["seeds"] = list(
                map(int, line.split(":")[1].strip().split(" "))
            )
            continue
        if ":" in line:
            key = line.split(":")[0].split(" ")[0]
            output[key] = {"source": [], "destination": [], "range": []}
            continue
        if line == "" or line == "\n" or line is None:
            continue
        values = list(map(int, line.split(" ")))
        output[key]["destination"].append(values[0])
        output[key]["source"].append(values[1])
        output[key]["range"].append(values[2])

    return output


def convert_seeds_part2(seeds):
    seed_output = []
    for i, seed in enumerate(seeds):
        if i % 2 == 0:
            start_seed = seed
        else:
            seed_output.extend(list(range(start_seed, start_seed + seed)))
    return seed_output


def seed_to_location(seed, maps):
    source = seed
    keys = list(maps.keys())[1:]
    destination = -1
    for i, key in enumerate(keys):
        for j in range(len(maps[key]["source"])):
            if (
                maps[key]["source"][j]
                <= source
                < maps[key]["source"][j] + maps[key]["range"][j]
            ):
                source_id = (
                    maps[key]["source"][j] + maps[key]["range"][j] - 1 - source
                )
                destination = (
                    maps[key]["destination"][j]
                    + maps[key]["range"][j]
                    - 1
                    - source_id
                )
        if destination == -1:
            destination = source
        source = destination
    return destination


def part1(file, part2=False):
    maps = parse_file(file)
    seed_to_location_map = {}
    if part2:
        for seed, _range in zip(maps["seeds"][::2], maps["seeds"][1::2]):
            for seed in range(seed, seed + _range):
                seed_to_location_map[seed] = seed_to_location(seed, maps)

    else:
        for seed in maps["seeds"]:
            seed_to_location_map[seed] = seed_to_location(seed, maps)
    return min(seed_to_location_map.values())


if __name__ == "__main__":
    print("Part 1: ", part1(read_file()))
    print("Part 2: ", part1(read_file(), part2=True))
