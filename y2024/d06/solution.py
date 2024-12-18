from aocd.models import Puzzle
from enum import Enum


def parse(data):
    floor_map = []
    start = (0, 0)
    rows = data.split("\n")
    for row_index in range(len(rows)):
        row = []
        for c in rows[row_index]:
            if c == '^':
                start = (row_index, rows[row_index].index('^'))
                row.append(".")
            else:
                row.append(c)

        floor_map.append(row)

    return floor_map, start


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    def __reversed__(self):
        if self == Direction.UP:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.UP
        elif self == Direction.LEFT:
            return Direction.RIGHT
        else:
            return Direction.LEFT


def determine_new_direction(old_direction):
    if old_direction == Direction.UP:
        return Direction.RIGHT
    elif old_direction == Direction.RIGHT:
        return Direction.DOWN
    elif old_direction == Direction.DOWN:
        return Direction.LEFT
    elif old_direction == Direction.LEFT:
        return Direction.UP


def move(start, floor_map):
    moves = []
    current = start
    inside = True
    moving = Direction.UP
    steps = 0
    while inside:
        steps += 1
        new_step = (current[0] + moving.value[0], current[1] + moving.value[1])
        if 0 <= new_step[0] < len(floor_map) and 0 <= new_step[1] < len(floor_map[0]):
            if floor_map[new_step[0]][new_step[1]] == '#':
                moving = determine_new_direction(moving)
            else:
                if moves.count(current) == 0:
                    moves.append(current)
                current = new_step
        else:
            if moves.count(current) == 0:
                moves.append(current)

            inside = False

    return moves


def part1(data):
    """Solve part 1."""
    print(data)
    start = data[1]
    moves = move(start, data[0])

    return len(moves)


def part2(data):
    """Solve part 2."""
    return 0


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
    if solution2 == int(6):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 6))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=6)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

