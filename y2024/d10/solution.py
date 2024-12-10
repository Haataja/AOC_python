from aocd.models import Puzzle


def parse(data):
    parsed_data = []
    starting_points = []
    data = data.split("\n")
    for row_index in range(len(data)):
        row = []
        for col_index in range(len(data[row_index])):
            number = int(data[row_index][col_index])
            row.append(number)
            if number == 0:
                starting_points.append((row_index, col_index))
        parsed_data.append(row)

    return parsed_data, starting_points


def part1(data):
    """Solve part 1."""
    number_sum = 0
    starting_points = data[1]
    top_map = data[0]
    for start in starting_points:
        tails = []
        new_trails = [[start]]
        while len(new_trails) > 0:
            trail = new_trails.pop()
            current = trail[-1]
            wanted_level = top_map[current[0]][current[1]] + 1
            if wanted_level == 10:
                if tails.count(current) == 0:
                    tails.append(current)
            else:
                if current[0] > 0:
                    # print("can go up")
                    if top_map[current[0] - 1][current[1]] == wanted_level:
                        new_trail = trail.copy()
                        new_trail.append((current[0] - 1, current[1]))
                        new_trails.append(new_trail)

                if current[0] < len(top_map) - 1:
                    # print("can go down {}{}".format(current, wanted_level))
                    if top_map[current[0] + 1][current[1]] == wanted_level:
                        new_trail = trail.copy()
                        new_trail.append((current[0] + 1, current[1]))
                        new_trails.append(new_trail)

                if current[1] > 0:
                    # print("can go left")
                    if top_map[current[0]][current[1] - 1] == wanted_level:
                        new_trail = trail.copy()
                        new_trail.append((current[0], current[1] - 1))
                        new_trails.append(new_trail)

                if current[1] < len(top_map[0]) - 1:
                    # print("can go right")
                    if top_map[current[0]][current[1] + 1] == wanted_level:
                        new_trail = trail.copy()
                        new_trail.append((current[0], current[1] + 1))
                        new_trails.append(new_trail)
        number_sum += len(tails)

    return number_sum


def part2(data):
    """Solve part 2."""
    number_sum = 0
    starting_points = data[1]
    top_map = data[0]
    for start in starting_points:
        trails = []
        new_trails = [[start]]
        while len(new_trails) > 0:
            trail = new_trails.pop()
            current = trail[-1]
            wanted_level = top_map[current[0]][current[1]] + 1
            if wanted_level == 10:
                trails.append(trail)
                # print("start {} tail {} {}".format(start, current, trail))
            else:
                if current[0] > 0:
                    # print("can go up")
                    if top_map[current[0] - 1][current[1]] == wanted_level:
                        new_trail = trail.copy()
                        new_trail.append((current[0] - 1, current[1]))
                        new_trails.append(new_trail)

                if current[0] < len(top_map) - 1:
                    # print("can go down {}{}".format(current, wanted_level))
                    if top_map[current[0] + 1][current[1]] == wanted_level:
                        new_trail = trail.copy()
                        new_trail.append((current[0] + 1, current[1]))
                        new_trails.append(new_trail)

                if current[1] > 0:
                    # print("can go left")
                    if top_map[current[0]][current[1] - 1] == wanted_level:
                        new_trail = trail.copy()
                        new_trail.append((current[0], current[1] - 1))
                        new_trails.append(new_trail)

                if current[1] < len(top_map[0]) - 1:
                    # print("can go right")
                    if top_map[current[0]][current[1] + 1] == wanted_level:
                        new_trail = trail.copy()
                        new_trail.append((current[0], current[1] + 1))
                        new_trails.append(new_trail)
        # print("{} {}".format(start, trails))
        number_sum += len(trails)
    return number_sum


def solve(puzzle_data):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_data)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


def test():
    test1_data = parse(
        """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    )  # puzzle.examples[0].input_data
    solution1 = part1(test1_data)
    if solution1 == int(puzzle.examples[0].answer_a):
        print("TEST 1: YES!")
    else:
        print("was {} should have been {}".format(solution1, puzzle.examples[0].answer_a))

    solution2 = part2(test1_data)
    if solution2 == int(81):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 31))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=10)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
