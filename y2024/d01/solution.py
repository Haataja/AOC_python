from aocd.models import Puzzle


def parse(data):
    rows = data.split()
    map1 = rows[0::2]
    map2 = rows[1::2]
    return map1, map2


def part1(data):
    """Solve part 1."""
    number_sum = 0
    map1 = data[0]
    map2 = data[1]
    map1.sort()
    map2.sort()
    for index in range(len(map1)):
        number_sum = number_sum + abs(int(map1[index]) - int(map2[index]))

    return number_sum


def part2(data):
    """Solve part 2."""
    number_sum = 0
    map1 = data[0]
    map2 = data[1]

    for location in map1:
        number_sum = number_sum + int(location) * map2.count(location)

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
    puzzle = Puzzle(year=2024, day=1)
    print(puzzle.examples[0])
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

