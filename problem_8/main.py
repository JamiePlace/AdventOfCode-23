from pathlib import Path
from typing import Dict, Tuple, List
part = "2"

def parse_input(part: str) -> Tuple[str, Dict[str, List[str]]]:
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
    code = lines[0].strip()
    keys = [l.split("=")[0].strip() for l in lines[2:]]
    maps = [l.split("=")[1].strip().replace("(", "").replace(")", "") for l in lines[2:]]
    lrmap = [lr.split(",") for lr in maps]
    lrmap = [[v[0].strip(), v[1].strip()] for v in lrmap]
    maps = {k:v for k,v in zip(keys, lrmap)}

    return code, maps

def main(part: str) -> int:
    code, maps = parse_input(part)
    path_map = {"L":0, "R": 1}
    keys = [k for k in list(maps.keys()) if k[-1] == "A"]
    targets = [k for k in list(maps.keys()) if k[-1] == "Z"]
    print(keys)
    print(targets)
    i=0
    while True:
        run = False
        for key in keys:
            if key[-1] != "Z":
                run = True
                break
        if not run:
            break

        idx = i % len(code)

        keys = [maps[key][path_map[code[idx]]] for key in keys]
        i += 1
        
    print(keys)
    return i

if __name__ == "__main__":
    print(main(part))
