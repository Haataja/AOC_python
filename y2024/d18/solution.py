from aocd.models import Puzzle
import re

from y2024.d06.solution import Direction


def parse(data):
    corrupted = []
    for row in data.split():
        corrupted.append((int(row.split(",")[1]), int(row.split(",")[0])))
    return corrupted


def part1(data, max_row, max_col, number_of_bytes):
    """Solve part 1."""
    for r_index in range(max_row + 1):
        row = []
        for c_index in range(max_col + 1):
            if (r_index, c_index) in data[:number_of_bytes]:
                row.append("#")
            else:
                row.append(".")
        print("".join(row))

    start = (0, 0)
    end = (max_row, max_col)
    visited = []
    routes = [(start, [start])]  # step, history
    ends = []
    min_steps = 0
    while len(routes) > 0:
        (current, history) = routes.pop(0)

        if current in list(map(lambda x: x[0], visited)):
            index = list(map(lambda x: x[0], visited)).index(current)
            if len(visited[index][1]) <= len(history):
                continue

        visited.append((current, history))
        if current == end:
            print("got in the end {}".format(history))
            ends.append(history)
            if min_steps == 0 or min_steps > len(history):
                min_steps = len(history)

        available = list(
            map(lambda x: (current[0] + x[0], current[1] + x[1]), [e.value for e in Direction]))
        filtered_steps = list(
            filter(lambda x: data[:number_of_bytes].count(x) == 0 and 0 <= x[0] <= max_row and 0 <= x[1] <= max_col, available))

        for step in filtered_steps:
            routes.append((step, history + [step]))
    return min_steps - 1


def part2(data, max_row, max_col, min_num_of_bytes):
    """Solve part 2."""
    number_of_bytes = min_num_of_bytes + 1
    while number_of_bytes < len(data):

        """ for r_index in range(max_row + 1):
            row = []
            for c_index in range(max_col + 1):
                if (r_index, c_index) in data[:number_of_bytes]:
                    row.append("#")
                else:
                    row.append(".")
            print("".join(row))
        print(number_of_bytes)"""

        start = (0, 0)
        end = (max_row, max_col)
        visited = []
        routes = [(start, [start])]  # step, history
        ends = []
        while len(routes) > 0:
            (current, history) = routes.pop(0)

            if current in visited:
                continue

            visited.append(current)
            if current == end:
                print("got in the end {}".format(history))
                ends.append(history)
                break

            available = list(
                map(lambda x: (current[0] + x[0], current[1] + x[1]), [e.value for e in Direction]))
            filtered_steps = list(
                filter(lambda x: data[:number_of_bytes].count(x) == 0 and 0 <= x[0] <= max_row and 0 <= x[1] <= max_col, available))

            for step in filtered_steps:
                routes.append((step, history + [step]))
        if len(ends) == 0:
            break
        else:
            number_of_bytes += 1

    return data[number_of_bytes - 1][1], data[number_of_bytes - 1][0]


def solve(puzzle_data):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_data)
    solution1 = part1(data, 70, 70, 1024)
    solution2 = part2(data, 70, 70, 1024)

    return solution1, solution2


def test():
    test1_data = parse(puzzle.examples[0].input_data)
    solution1 = part1(test1_data, 6, 6, 12)
    if solution1 == int(22):
        print("TEST 1: YES!")
    else:
        print("was {} should have been {}".format(solution1, 22))

    test2_data = parse(puzzle.examples[0].input_data)
    solution2 = part2(test2_data, 6, 6, 12)
    if solution2 == int(31):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 31))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=18)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
