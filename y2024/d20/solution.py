from aocd.models import Puzzle
from y2024.d06.solution import Direction


def parse(data):
    rows = data.split()
    walls = []
    for row in range(len(rows)):
        for col in range(len(rows[row])):
            if rows[row][col] == "#":
                walls.append((row, col))
            elif rows[row][col] == "S":
                start = (row, col)
            elif rows[row][col] == "E":
                end = (row, col)

    return start, end, walls


def part1(data):
    """Solve part 1."""
    number_sum = 0
    (start, end, walls) = data
    for r in range(15):
        row = []
        for c in range(15):
            if (r, c) in walls:
                row.append("#")
            elif (r, c) == start:
                row.append("S")
            elif (r, c) == end:
                row.append("E")
            else:
                row.append(".")
        print("".join(row))

    current = start
    steps = [start]
    while current != end:
        direction = list(map(lambda x: (current[0] + x[0], current[1] + x[1]), [e.value for e in Direction]))
        step = list(filter(lambda x: x not in walls and x not in steps, direction))
        steps.append(step[0])
        current = step[0]



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
    if solution1 == puzzle.examples[0].answer_a:
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
    puzzle = Puzzle(year=2024, day=20)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    #solutions = solve(puzzle_input)
    #print("\n".join(str(solution) for solution in solutions))