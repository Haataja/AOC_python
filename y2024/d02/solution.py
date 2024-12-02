from aocd.models import Puzzle


def parse(data):
    return data.split("\n")


def find_breaking_index(levels):
    safe = True
    is_increasing = False
    level_index = 0
    for level_index in range(len(levels) - 1):
        level_diff = int(levels[level_index]) - int(levels[level_index + 1])
        # print(levels[level_index] + " {}".format(level_diff))
        if abs(level_diff) > 3 or level_diff == 0:
            safe = False
            break
        else:
            if level_index == 0:
                if level_diff < 0:
                    is_increasing = True
            else:
                if is_increasing:
                    if level_diff > 0:
                        safe = False
                        break
                else:
                    if level_diff < 0:
                        safe = False
                        break

    return safe, level_index

def part1(data):
    """Solve part 1."""
    number_sum = 0
    for report in data:
        (s, i) = find_breaking_index(report.split())

        if s:
            number_sum = number_sum + 1

    return number_sum


def part2(data):
    """Solve part 2."""
    number_sum = 0
    for report in data:
        levels = report.split()
        (s, i) = find_breaking_index(levels)
        if s:
            # print("default safe   {}".format(levels))
            number_sum += 1
        else:
            a1 = levels.copy()
            del a1[i]
            (s1, i1) = find_breaking_index(a1)
            if s1:
                # print("safe removing i {}   {}".format(i, a1))
                number_sum += 1
            else:
                a2 = levels.copy()
                del a2[i + 1]
                (s2, i2) = find_breaking_index(a2)
                if s2:
                    # print("safe removing i+1 {} {}".format(i +1, a2))
                    number_sum += 1
                elif i > 0:
                    a3 = levels.copy()
                    del a3[i - 1]
                    (s3, i3) = find_breaking_index(a3)
                    if s3:
                        # print("safe by removing i-1 {}  {}".format(i-1, a3))
                        number_sum += 1

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
    if solution2 == int(4):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 4))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=2)
    print(puzzle.examples[0])
    test()

    # hard lines to notice
    # "12 10 12 14 15 16 19 22\n66 67 68 71 72 69\n52 47 49 46 43 41 40\n69 73 75 77 78 81 83 86\n75 77 72 70 69"
    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
