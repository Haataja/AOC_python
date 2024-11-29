from aocd.models import Puzzle


def parse(data):
    return data.split()


def part1(data):
    """Solve part 1."""
    number_sum = 0
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


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=1)
    print(puzzle.examples[0])
    puzzle_input = puzzle.examples[0].input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

