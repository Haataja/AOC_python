from aocd.models import Puzzle


def parse(data):
    (available, designs) = data.split("\n\n")
    towels = available.replace(" ","").split(",")
    designs = designs.split("\n")
    return towels, designs

def check_if_possible(design, towels, length_of_towels):
    index = 1
    while index <= len(design):
        if index > length_of_towels:
            return False
        sub_design = design[:index]
        # print("{} {} {} {}".format(index, design, design[index:], len(design[index:])))
        if sub_design in towels:
            next_design = design[index:]
            if len(next_design) > 0:
                if check_if_possible(design[index:], towels, length_of_towels):
                    return True
            else:
                return True
        index += 1

    return False

def part1(data):
    """Solve part 1."""
    number_sum = 0
    (towels, designs) = data
    length_of_towels = max(list(map(lambda x: len(x), towels)))
    print("max length of towels ", length_of_towels)
    for design in designs:
        print("Checking for {}".format(design))
        if check_if_possible(design, towels, length_of_towels):
            print("got true: {}".format(design))
            number_sum += 1

    return number_sum


def part2(data):
    """Solve part 2."""
    number_sum = 0

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
    puzzle = Puzzle(year=2024, day=19)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))