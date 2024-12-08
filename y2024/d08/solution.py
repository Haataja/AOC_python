from aocd.models import Puzzle


def parse(data):
    antennas = []
    rows = data.split("\n")
    for row_index in range(len(rows)):
        for c_index in range(len(rows[row_index])):
            if rows[row_index][c_index] != '.':
                antenna_chars = list(map(lambda x: x[0], antennas))
                if antenna_chars.count(rows[row_index][c_index]) > 0:
                    antenna = antennas[antenna_chars.index(rows[row_index][c_index])]
                    antenna[1].append((row_index, c_index))
                else:
                    antennas.append((rows[row_index][c_index], [(row_index, c_index)]))

    return antennas, len(rows) - 1, len(rows[0]) - 1


def part1(data):
    """Solve part 1."""
    antennas = data[0]
    max_row = data[1]
    max_col = data[2]
    antinodes = []

    for antenna in antennas:
        antenna_list = antenna[1]
        for point_index in range(len(antenna_list)):
            point = antenna_list[point_index]
            remaining_list = antenna_list[point_index + 1:]
            for remaining in remaining_list:
                row_diff = point[0] - remaining[0]
                col_diff = point[1] - remaining[1]
                # print("{} {} {} {}".format(point, remaining, row_diff, col_diff))
                if 0 <= point[0] + row_diff <= max_row and 0 <= point[1] + col_diff <= max_col:
                    antinode_1 = (point[0] + row_diff, point[1] + col_diff)
                    if antinodes.count(antinode_1) == 0 and antenna_list.count(antinode_1) == 0:
                        antinodes.append(antinode_1)
                if 0 <= remaining[0] - row_diff <= max_row and 0 <= remaining[1] - col_diff <= max_col:
                    antinode_2 = (remaining[0] - row_diff, remaining[1] - col_diff)
                    if antinodes.count(antinode_2) == 0 and antenna_list.count(antinode_2) == 0:
                        antinodes.append(antinode_2)

    # print(antinodes)
    for row in range(max_row + 1):
        print_row = []
        for col in range(max_col + 1):
            if antinodes.count((row, col)) > 0:
                print_row.append("#")
            else:
                print_row.append(".")
        print("".join(print_row))
    return len(antinodes)


def part2(data):
    """Solve part 2."""
    antennas = data[0]
    all_antenna_points = []
    for antenna in antennas:
        for point in antenna[1]:
            all_antenna_points.append(point)
    max_row = data[1]
    max_col = data[2]
    antinodes = []
    antenna_count = 0

    for antenna in antennas:
        antenna_list = antenna[1]
        antenna_count += len(antenna_list)
        for point_index in range(len(antenna_list)):
            point = antenna_list[point_index]
            remaining_list = antenna_list[point_index + 1:]
            for remaining in remaining_list:
                row_diff = point[0] - remaining[0]
                col_diff = point[1] - remaining[1]
                # print("{} {} {} {}".format(point, remaining, row_diff, col_diff))
                antinode_1 = (point[0] + row_diff, point[1] + col_diff)
                while 0 <= antinode_1[0] <= max_row and 0 <= antinode_1[1] <= max_col:
                    if antinodes.count(antinode_1) == 0 and all_antenna_points.count(antinode_1) == 0:
                        antinodes.append(antinode_1)
                    antinode_1 = (antinode_1[0] + row_diff, antinode_1[1] + col_diff)

                antinode_2 = (remaining[0] - row_diff, remaining[1] - col_diff)
                while 0 <= antinode_2[0] <= max_row and 0 <= antinode_2[1] <= max_col:
                    if antinodes.count(antinode_2) == 0 and all_antenna_points.count(antinode_2) == 0:
                        antinodes.append(antinode_2)
                    antinode_2 = (antinode_2[0] - row_diff, antinode_2[1] - col_diff)

    for row in range(max_row + 1):
        print_row = []
        for col in range(max_col + 1):
            if antinodes.count((row, col)) > 0:
                print_row.append("#")
            else:
                print_row.append(".")
        print("".join(print_row))
    return len(antinodes) + antenna_count


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
    if solution2 == int(34):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 34))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=8)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

