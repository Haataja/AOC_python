from aocd.models import Puzzle
import re


def parse(data):
    return data


def part1(data):
    """Solve part 1."""
    number_sum = 0
    uncorrupted = re.findall('mul\\(\\d+,\\d+\\)', data)
    for mul in uncorrupted:
        (x, y) = mul.replace("mul(", "").replace(")", "").split(",")
        number_sum += int(x) * int(y)

    return number_sum


def part2(data):
    """Solve part 2."""
    number_sum = 0
    uncorrupted = re.findall("mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\)", data)
    print(uncorrupted)
    calculate = True
    for mul in uncorrupted:
        if mul == "do()":
            calculate = True
        elif mul == "don't()":
            calculate = False
        elif calculate:
            (x, y) = mul.replace("mul(", "").replace(")", "").split(",")
            number_sum += int(x) * int(y)
    return number_sum


def solve(puzzle_data):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_data)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


def test():
    test1_data = parse(puzzle.examples[0].input_data)
    solution1 = part1(test1_data)
    if solution1 == 161:  # int(puzzle.examples[0].answer_a):
        print("TEST 1: YES!")
    else:
        print("was {} should have been {}".format(solution1, puzzle.examples[0].answer_a))

    test2_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))" # parse(puzzle.examples[0].input_data)
    solution2 = part2(test2_data)
    if solution2 == int(48):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 31))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=3)
    print(puzzle.examples[0])
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
