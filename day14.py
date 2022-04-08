from typing import IO, Dict, List, Tuple
from collections import Counter

# Type alias for pair insertion rules
Rules = Dict[str, str]


def parse_rule(rule_string: str) -> List[str]:
    return rule_string.strip().split(" -> ")


def read_puzzle_input(puzzle_input_file: IO[str]) -> Tuple[str, Rules]:
    polymer_template = puzzle_input_file.readline().strip()
    puzzle_input_file.readline()  # Blank line
    rules = dict(map(parse_rule, puzzle_input_file.readlines()))
    return (polymer_template, rules)


def pair_insertion(polymer: str, rules: Rules) -> str:
    new_polymer = ""
    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        middle_char = rules[pair]
        new_polymer += pair[0] + middle_char
    new_polymer += polymer[-1]
    return new_polymer


def main():
    with open("puzzle-input-day14.txt") as puzzle_input_file:
        polymer_template, rules = read_puzzle_input(puzzle_input_file)
    pair_insertion_step_count = 10
    polymer = polymer_template
    for _ in range(pair_insertion_step_count):
        polymer = pair_insertion(polymer, rules)
    ordered_letter_counts = Counter(polymer).most_common()
    print(ordered_letter_counts[0][1] - ordered_letter_counts[-1][1])


if __name__ == "__main__":
    main()
