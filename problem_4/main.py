from pathlib import Path


def read_file():
    path = Path(__file__).parent / "input.txt"
    with open(path, "r") as f:
        lines = f.readlines()
    for line in lines:
        yield line


def number_line_to_list(line):
    return [int(i) for i in line.split(" ") if i != ""]


def parse_cards():
    strings = read_file()
    cards = []
    for string in strings:
        card_id = string.split(":")[0]
        numbers = string.split(":")[1]
        winning_numbers = numbers.split("|")[0]
        my_numbers = numbers.split("|")[1]

        winning_numbers = number_line_to_list(winning_numbers)
        my_numbers = number_line_to_list(my_numbers)
        cards.append((card_id, winning_numbers, my_numbers))
    return cards


def count_winning_numbers(card):
    winning_numbers = card[1]
    my_numbers = card[2]
    score = 0
    for number in my_numbers:
        if number in winning_numbers:
            score += 1
    return score


def part1():
    strings = read_file()
    score_sum = 0
    for string in strings:
        score = -1
        numbers = string.split(":")[1]
        winning_numbers = numbers.split("|")[0]
        my_numbers = numbers.split("|")[1]

        winning_numbers = number_line_to_list(winning_numbers)
        my_numbers = number_line_to_list(my_numbers)
        for number in my_numbers:
            if number in winning_numbers:
                score += 1
        if score > -1:
            score_sum += 2**score
    return score_sum


def count_cards_to_grab(key, cards_to_grab: dict):
    values = cards_to_grab[key]
    _sum = len(values)
    if len(values) == 0:
        return 0
    for val in values:
        _sum += count_cards_to_grab(val, cards_to_grab)
    return _sum


def part2():
    cards = parse_cards()
    winning_numbers = []
    for i, card in enumerate(cards):
        winning_numbers.append(count_winning_numbers(card))
    cards_to_grab = {}
    orig_instances = len(cards)
    for i, num in enumerate(winning_numbers):
        ctg = list(range(i + 2, i + num + 2))
        cards_to_grab[i + 1] = ctg

    _sum = 0
    for i in range(1, len(cards) + 1):
        _sum += count_cards_to_grab(i, cards_to_grab)

    return _sum + orig_instances


if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())
