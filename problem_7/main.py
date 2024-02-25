import sys
import math
from pathlib import Path
from typing import List, Tuple
from collections import Counter

part = "1"

def parse_input(part: str) -> Tuple[List[str], List[int]]:
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
    split_lines = [l.strip().split(" ") for l in lines]

    cards = [c[0] for c in split_lines]
    bet = [int(c[1]) for c in split_lines]
    return cards, bet

def type_of_hand(counter: Counter) -> str:
    if len(counter) == 1:
        return "Five of a Kind"
    elif len(counter) == 2:
        if 2 in counter.values():
            return "Full House"
        else:
            return "Four of a Kind"
    elif len(counter) == 3:
        if 3 in counter.values():
            return "Three of a Kind"
        else:
            return "Two Pair"
    elif len(counter) == 4:
        return "One Pair"
    else:
        return "High Card"

def type_score(hand: str) -> int:
    if hand == "Five of a Kind":
        return 100
    elif hand == "Four of a Kind":
        return 80
    elif hand == "Full House":
        return 60
    elif hand == "Three of a Kind":
        return 40
    elif hand == "Two Pair":
        return 20
    elif hand == "One Pair":
        return 10
    else:
        return 0

def card_score(card: str) -> int:
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 1
    elif card == "T":
        return 10
    else:
        return int(card)

def score_hand(cards: str) -> int:
    counter = Counter(list(cards))
    # handle J wildcards
    wildcard = None
    if "J" in counter:
        possible_values = [c for c in counter]
        score = {}
        for c in possible_values:
            temp_counter = counter.copy()
            if c != "J":
                temp_counter[c] += temp_counter["J"]
                temp_counter.pop("J")
            # if there are equivalent hand scores, find the one with the best cards in order
            score[c] = type_score(type_of_hand(temp_counter))
        wildcard = max(score, key=score.get) # type: ignore

    if wildcard:
        if wildcard == "J":
            pass
        counter[wildcard] += counter["J"]
        counter.pop("J")

    hand = type_of_hand(counter)
    hand_score = type_score(hand)
    return hand_score

def compare_hands(hand1: str, hand2: str) -> bool:
    for c1, c2 in zip(list(hand1), list(hand2)):
        if card_score(c1) == card_score(c2):
            continue
        if card_score(c1) > card_score(c2):
            return False
        if card_score(c1) < card_score(c2):
            return True
    return True

def main(part: str = "1"):
    cards, bet = parse_input(part)
    for i in range(len(cards)):
        if i == 0:
            continue
        pointer = i
        for j in range(i-1, -1, -1):
            if score_hand(cards[pointer]) < score_hand(cards[j]):
                cards[pointer], cards[j] = cards[j], cards[pointer]
                bet[pointer], bet[j] = bet[j], bet[pointer]
                pointer = j
            if score_hand(cards[pointer]) == score_hand(cards[j]):
                if compare_hands(cards[pointer], cards[j]):
                    cards[pointer], cards[j] = cards[j], cards[pointer]
                    bet[pointer], bet[j] = bet[j], bet[pointer]
                    pointer = j
    return sum([b*(i+1) for i,b in enumerate(bet)])

        
if __name__ == "__main__":
    print(main(part))
