from pathlib import Path
import numpy as np
from collections import deque

coords = [
    np.array([0, -1]),  # down
    np.array([0, 1]),  # up
    np.array([-1, 0]),  # left
    np.array([1, 0]),  # right
    np.array([-1, -1]),  # left down
    np.array([1, 1]),  # right up
    np.array([1, -1]),  # right down
    np.array([-1, 1]),  # left up
]


def read_file():
    path = Path(__file__).parent / "input.txt"
    with open(path, "r") as f:
        lines = f.readlines()
    for line in lines:
        yield line


def concat_strings():
    strings = read_file()

    all_strings = []
    for string in strings:
        all_strings.append(list(string.strip()))
    return np.vstack(all_strings)


def get_neighbours(x, y, block, index=False):
    neighbours = []
    index_val = []
    for coord in coords:
        try:
            neighbours.append(block[x + coord[0], y + coord[1]])
            index_val.append((x + coord[0], y + coord[1]))
        except IndexError:
            pass
    if index:
        return neighbours, index_val
    return neighbours


def is_number(char):
    try:
        int(char)
        return True
    except ValueError:
        return False


def is_period(char):
    return char == "."


def is_star(char):
    return char == "*"


def has_symbol_neighbour(points, block):
    neighbours = get_neighbours(points[0], points[1], block)
    return any(
        [True for x in neighbours if not is_period(x) and not is_number(x)]
    )


def find_star_index(x, y, block):
    neighbours, index_val = get_neighbours(x, y, block, index=True)
    for neighbour in list(zip(neighbours, index_val)):
        if is_star(neighbour[0]):
            return neighbour[1]


def make_number(num_coords, block, gear=False):
    searched_coords = []
    numbers_found = []
    symbols_found = []
    for x, y in list(zip(*np.where(num_coords))):
        if (x, y) in searched_coords:
            continue
        symbol_index = []
        str_num = deque()
        str_num.append(block[x, y])
        searched_coords.append((x, y))
        symbol_index.append(find_star_index(x, y, block))
        # looking ahead
        try:
            i = 1
            while is_number(block[x, y + i]):
                if (x, y + i) in searched_coords:
                    break
                symbol_index.append(find_star_index(x, y + i, block))
                str_num.append(block[x, y + i])
                searched_coords.append((x, y + i))
                i += 1
        except IndexError:
            pass

        # looking back
        try:
            i = 1
            while is_number(block[x, y - i]):
                if (x, y - i) in searched_coords:
                    break
                symbol_index.append(find_star_index(x, y - i, block))
                str_num.appendleft(block[x, y - i])
                searched_coords.append((x, y - i))
                i += 1
        except IndexError:
            pass
        numbers_found.append(int("".join(str_num)))
        symbol_index = list(filter(None, symbol_index))
        symbol_index = list(set(symbol_index))
        symbols_found.append(symbol_index)
    index_count = {}
    for index in symbols_found:
        if len(index) == 0:
            continue
        for i in index:
            if str(i) not in index_count.keys():
                index_count[str(i)] = 1
            else:
                index_count[str(i)] += 1
    index_count = {k: v for k, v in index_count.items() if v == 2}
    gear_numbers = []
    for star_coords in index_count.keys():
        # star_coords are strings of tuples
        star_coords = eval(star_coords)
        gear_num_cache = 1
        for i, val in enumerate(symbols_found):
            for sub_val in val:
                if sub_val == star_coords:
                    gear_num_cache *= numbers_found[i]
        gear_numbers.append(gear_num_cache)

    if gear:
        return gear_numbers
    return numbers_found


def part1():
    block = concat_strings()
    point_coords = []
    for i in range(block.shape[0]):
        for j in range(block.shape[1]):
            point_coords.append((i, j))
    number_block = np.vectorize(is_number)(block)
    symbol_neighbours = np.array(
        list(map(lambda x: has_symbol_neighbour(x, block), point_coords))
    )
    symbol_neighbours = symbol_neighbours.reshape(block.shape)

    numbers_with_neighbours = np.logical_and(number_block, symbol_neighbours)
    return sum(make_number(numbers_with_neighbours, block))


def part2():
    block = concat_strings()
    point_coords = []
    for i in range(block.shape[0]):
        for j in range(block.shape[1]):
            point_coords.append((i, j))
    number_block = np.vectorize(is_number)(block)
    symbol_neighbours = np.array(
        list(map(lambda x: has_symbol_neighbour(x, block), point_coords))
    )
    symbol_neighbours = symbol_neighbours.reshape(block.shape)

    numbers_with_neighbours = np.logical_and(number_block, symbol_neighbours)
    return sum(make_number(numbers_with_neighbours, block, gear=True))


if __name__ == "__main__":
    print("part 1: ", part1())
    print("part 2: ", part2())
