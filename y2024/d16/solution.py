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
    #print(data)
    end = data[1]
    end_paths = []
    walls = data[2]
    direction = Direction.RIGHT
    visited = [] # (current, score)
    paths = [(data[0], [data[0]], direction, 0)]
    path_min = 0
    i = 0
    while len(paths) > 0:
        print(len(paths))
        ((r, c), history, cur_dir, score) = paths.pop(0)

        if (r, c) in list(map(lambda x: x[0], visited)):
            index = list(map(lambda x: x[0], visited)).index((r, c))
            if score > visited[index][1]:
                continue

        if (r, c) == end:
            print("got to the end {} {}".format(score, history))
            end_paths.append(history)
            if path_min == 0 or path_min > score:
                path_min = score
            continue

        visited.append(((r, c), score))

        available = list(
            map(lambda x: ((r + x[0], c + x[1]), Direction(x)), list(filter(lambda  y: y != cur_dir.__reversed__().value ,[e.value for e in Direction]))))
        available = list(filter(lambda x: walls.count(x[0]) == 0, available))
        #  print("current {}, {}, available {}".format((r,c), cur_dir, available))
        if len(available) > 0:
            for step in available:
                if step[1] == cur_dir:
                    new_score = score + 1
                else:
                    new_score = score + 1001
                paths.append((step[0], history + [step[0]], step[1], new_score))
        i += 1

    return path_min


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
    if solution1 == int(7036):
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
    puzzle = Puzzle(year=2024, day=16)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
