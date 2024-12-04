from aocd.models import Puzzle


def parse(data):
    rows = data.split("\n")
    return rows


def check_for_xmas(row_index, col_index, data):
    # check to right
    s = 0
    if col_index + 1 < len(data[row_index]):
        if data[row_index][col_index + 1] == 'M':
            if col_index + 2 < len(data[row_index]):
                if data[row_index][col_index + 2] == 'A':
                    if col_index + 3 < len(data[row_index]):
                        if data[row_index][col_index + 3] == 'S':
                            s += 1
    # check to left
    if col_index - 1 >= 0:
        if data[row_index][col_index - 1] == 'M':
            if col_index - 2 >= 0:
                if data[row_index][col_index - 2] == 'A':
                    if col_index - 3 >= 0:
                        if data[row_index][col_index - 3] == 'S':
                            s += 1
    # check up
    if row_index - 1 >= 0:
        if data[row_index - 1][col_index] == 'M':
            if row_index - 2 >= 0:
                if data[row_index - 2][col_index] == 'A':
                    if row_index - 3 >= 0:
                        if data[row_index - 3][col_index] == 'S':
                            s += 1
    # check down
    if row_index + 1 < len(data):
        if data[row_index + 1][col_index] == 'M':
            if row_index + 2 < len(data):
                if data[row_index + 2][col_index] == 'A':
                    if row_index + 3 < len(data):
                        if data[row_index + 3][col_index] == 'S':
                            s += 1
    # check diagonal right up
    if col_index + 1 < len(data[row_index]) and row_index - 1 >= 0:
        if data[row_index - 1][col_index + 1] == 'M':
            if col_index + 2 < len(data[row_index]) and row_index - 2 >= 0:
                if data[row_index - 2][col_index + 2] == 'A':
                    if col_index + 3 < len(data[row_index]) and row_index - 3 >= 0:
                        if data[row_index - 3][col_index + 3] == 'S':
                            s += 1
    # check diagonal right down
    if col_index + 1 < len(data[row_index]) and row_index + 1 < len(data):
        if data[row_index + 1][col_index + 1] == 'M':
            if col_index + 2 < len(data[row_index]) and row_index + 2 < len(data):
                if data[row_index + 2][col_index + 2] == 'A':
                    if col_index + 3 < len(data[row_index]) and row_index + 3 < len(data):
                        if data[row_index + 3][col_index + 3] == 'S':
                            s += 1
    # check diagonal left up
    if col_index - 1 >= 0 and row_index - 1 >= 0:
        if data[row_index - 1][col_index - 1] == 'M':
            if col_index - 2 >= 0 and row_index - 2 >= 0:
                if data[row_index - 2][col_index - 2] == 'A':
                    if col_index - 3 >= 0 and row_index - 3 >= 0:
                        if data[row_index - 3][col_index - 3] == 'S':
                            s += 1
    # check diagonal left down
    if col_index - 1 >= 0 and row_index + 1 < len(data):
        if data[row_index + 1][col_index - 1] == 'M':
            if col_index - 2 >= 0 and row_index + 2 < len(data):
                if data[row_index + 2][col_index - 2] == 'A':
                    if col_index - 3 >= 0 and row_index + 3 < len(data):
                        if data[row_index + 3][col_index - 3] == 'S':
                            s += 1
    # print("{} {} {} ".format(row_index, col_index, s))
    return s


def part1(data):
    """Solve part 1."""
    number_sum = 0
    for row_index in range(len(data)):
        # print(data[row_index])
        for col_index in range(len(data[row_index])):
            if data[row_index][col_index] == 'X':
                number_sum += check_for_xmas(row_index, col_index, data)

    return number_sum


def check_for_x(row_index, col_index, data):
    s = 0
    if row_index - 1 >= 0 and col_index - 1 >= 0:
        left_up_corner = data[row_index - 1][col_index - 1]
        if left_up_corner == 'M' or left_up_corner == 'S':
            right_down_corner = 'S'
            if left_up_corner == 'S':
                right_down_corner = 'M'
            if row_index + 1 < len(data) and col_index + 1 < len(data[row_index]):
                if data[row_index + 1][col_index + 1] == right_down_corner:
                    if col_index + 1 < len(data[row_index]):
                        right_up_corner = data[row_index - 1][col_index + 1]
                        if right_up_corner == 'M' or right_up_corner == 'S':
                            left_down_corner = 'S'
                            if right_up_corner == 'S':
                                left_down_corner = 'M'
                            if data[row_index + 1][col_index - 1] == left_down_corner:
                                s += 1

    return s


def part2(data):
    """Solve part 2."""
    number_sum = 0
    for row_index in range(len(data)):
        for col_index in range(len(data[row_index])):
            if data[row_index][col_index] == 'A':
                number_sum += check_for_x(row_index, col_index, data)
    return number_sum


def solve(puzzle_data):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_data)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


def test():
    test1_data = parse("""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""")
    solution1 = part1(test1_data)
    if solution1 == int(18):
        print("TEST 1: YES!")
    else:
        print("was {} should have been {}".format(solution1, puzzle.examples[0].answer_a))

    solution2 = part2(test1_data)
    if solution2 == int(9):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 31))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=4)
    print(puzzle.examples[0])
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

