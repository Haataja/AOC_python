from aocd.models import Puzzle


def parse(data):
    return data.split("\n")


def permutations(target, s, number_index, numbers):
    # print("{} {} {} {} {}".format(target, s, number_index, numbers, len(numbers)))
    if number_index == len(numbers):
        return len(list(filter(lambda x: x == target, s))) > 0

    sums = []
    for operation in s:
        if operation + numbers[number_index] <= target:
            sums.append(operation + numbers[number_index])
        if operation * numbers[number_index] <= target:
            sums.append(operation * numbers[number_index])

    if len(sums) == 0:
        return False

    return permutations(target, sums, number_index + 1, numbers)


def permutations_with_concat(target, s, number_index, numbers):
    # print("{} {} {} {} {}".format(target, s, number_index, numbers, len(numbers)))
    if number_index == len(numbers):
        return len(list(filter(lambda x: x == target, s))) > 0

    sums = []
    for operation in s:
        if operation + numbers[number_index] <= target:
            sums.append(operation + numbers[number_index])
        if operation * numbers[number_index] <= target:
            sums.append(operation * numbers[number_index])
        concat = str(operation) + str(numbers[number_index])
        if int(concat) <= target:
            sums.append(int(concat))

    if len(sums) == 0:
        return False

    return permutations_with_concat(target, sums, number_index + 1, numbers)


def part1(data):
    """Solve part 1."""
    number_sum = 0
    for row in data:
        (v, n) = row.split(":")
        numbers = list(map(lambda x: int(x), n.split()))
        if permutations(int(v), [numbers[0]], 1, numbers):
            number_sum += int(v)

    return number_sum


def part2(data):
    """Solve part 2."""
    number_sum = 0
    for row in data:
        (v, n) = row.split(":")
        numbers = list(map(lambda x: int(x), n.split()))
        if permutations_with_concat(int(v), [numbers[0]], 1, numbers):
            number_sum += int(v)

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
    if solution2 == int(11387):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 11387))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=7)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

