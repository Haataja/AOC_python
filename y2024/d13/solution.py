from aocd.models import Puzzle
import re


def parse(data):
    machines = data.split("\n\n")
    parsed = []
    for machine in machines:
        rows = machine.split("\n")
        a = re.findall("\\d+", rows[0])
        b = re.findall("\\d+", rows[1])
        goal = re.findall("\\d+", rows[2])
        parsed.append((a, b, goal))

    return parsed


def part1(data):
    """Solve part 1."""
    number_sum = 0
    for machine in data:
        (ax, ay) = machine[0]
        (bx, by) = machine[1]
        (x, y) = machine[2]
        b = (int(y)*int(ax) - int(ay)*int(x))/(int(ax)*int(by) - int(ay)*int(bx))
        if b.is_integer():
            a = (int(x) - int(bx) * int(b)) / int(ax)
            number_sum += 3 * int(a) + int(b)
    return number_sum


def part2(data):
    """Solve part 2."""
    number_sum = 0
    for machine in data:
        (ax, ay) = machine[0]
        (bx, by) = machine[1]
        (x, y) = machine[2]
        b = ((int(y) + 10000000000000)*int(ax) - int(ay)*(int(x) + 10000000000000))/(int(ax)*int(by) - int(ay)*int(bx))
        if b.is_integer():
            a = ((int(x) + 10000000000000) - int(bx) * int(b)) / int(ax)
            number_sum += 3 * int(a) + int(b)

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
    if solution1 == int(puzzle.examples[0].answer_a):
        print("TEST 1: YES!")
    else:
        print("was {} should have been {}".format(solution1, puzzle.examples[0].answer_a))

    test2_data = parse(puzzle.examples[0].input_data)
    solution2 = part2(test2_data)
    if solution2 == int(31):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 31))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=13)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
