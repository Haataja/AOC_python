from aocd.models import Puzzle


def parse(data):
    robots = []
    for robot in data.split("\n"):
        (p, v) = robot.split()
        p = p.replace("p=", "")
        (x, y) = p.split(",")
        v = v.replace("v=", "")
        (vx, vy) = v.split(",")
        robots.append(((int(y), int(x)), (int(vy), int(vx))))
    return robots


def move_robot(robot, max_rows, max_cols):
    new_row = robot[0][0] + robot[1][0]
    new_col = robot[0][1] + robot[1][1]
    if new_row < 0:
        new_row = max_rows + new_row
    elif new_row >= max_rows:
        new_row = new_row - max_rows

    if new_col < 0:
        new_col = max_cols + new_col
    elif new_col >= max_cols:
        new_col = new_col - max_cols

    return (new_row, new_col), robot[1]


def part1(data, max_rows, max_cols):
    """Solve part 1."""
    number_sum = 0
    print(data)
    robots = []
    robot_places = list(map(lambda x: x[0], data))
    for r_index in range(max_rows):
        row = []
        for c_index in range(max_cols):
            r_count = robot_places.count((r_index, c_index))
            if r_count == 0:
                row.append(".")
            else:
                row.append(str(r_count))
        print("".join(row))

    for i in range(100):
        for robot in data:
            robots.append(move_robot(robot, max_rows, max_cols))

        data = robots.copy()
        robots.clear()

    print(data)
    middle_row = int(max_rows / 2)
    middle_col = int(max_cols / 2)
    first = []
    second = []
    third = []
    fourth = []
    for robot in data:
        if robot[0][0] < middle_row and robot[0][1] < middle_col:
            first.append(robot)
        elif robot[0][0] < middle_row and robot[0][1] > middle_col:
            second.append(robot)
        elif robot[0][0] > middle_row and robot[0][1] < middle_col:
            third.append(robot)
        elif robot[0][0] > middle_row and robot[0][1] > middle_col:
            fourth.append(robot)
    print(middle_row, middle_col, len(first), len(second), len(third), len(fourth))

    robot_places = list(map(lambda x: x[0], data))
    for r_index in range(max_rows):
        row = []
        for c_index in range(max_cols):
            r_count = robot_places.count((r_index, c_index))
            if r_count == 0:
                row.append(".")
            else:
                row.append(str(r_count))
        print("".join(row))

    return len(first) * len(second) * len(third) * len(fourth)


def part2(data):
    """Solve part 2."""
    number_sum = 0
    robots = []
    for i in range(6446):
        for robot in data:
            robots.append(move_robot(robot, 103, 101))

        data = robots.copy()
        robots.clear()
        if i > 6000:
            robot_places = list(map(lambda x: x[0], data))
            for r_index in range(103):
                row = []
                for c_index in range(101):
                    r_count = robot_places.count((r_index, c_index))
                    if r_count == 0:
                        row.append(".")
                    else:
                        row.append(str(r_count))
                print("".join(row))
            print(i)
            # x = input() made a gues for the min of the prints and used input to slow down the printing

    return number_sum


def solve(puzzle_data):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_data)
    solution1 = part1(data, 103, 101)
    solution2 = part2(data)

    return solution1, solution2


def test():
    test1_data = parse(puzzle.examples[0].input_data)
    solution1 = part1(test1_data, 7, 11)
    if solution1 == int(12):
        print("TEST 1: YES!")
    else:
        print("was {} should have been {}".format(solution1, puzzle.examples[0].answer_a))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=14)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
