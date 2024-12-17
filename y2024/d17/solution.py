from aocd.models import Puzzle
import re


def parse(data):
    rows = data.split("\n")
    register_a = int(re.findall("\\d+", rows[0])[0])
    register_b = int(re.findall("\\d+", rows[1])[0])
    register_c = int(re.findall("\\d+", rows[2])[0])
    program = list(map(lambda x: int(x), rows[4][9:].split(",")))

    return register_a, register_b, register_c, program


def part1(data):
    """Solve part 1."""
    results = []
    (register_a, register_b, register_c, program) = data
    print(data)
    op_index = 0
    while op_index < len(program):
        opcode = program[op_index]
        operand = program[op_index + 1]
        if 0 <= operand <= 3:
            combo_operand = operand
        elif operand == 4:
            combo_operand = register_a
        elif operand == 5:
            combo_operand = register_b
        elif operand == 6:
            combo_operand = register_c

        if opcode == 0:
            result = register_a / pow(2, combo_operand)
            register_a = int(result)
        elif opcode == 1:
            result = register_b ^ operand
            register_b = result
        elif opcode == 2:
            result = combo_operand % 8
            register_b = result
        elif opcode == 3:
            if register_a != 0:
                op_index = operand - 2
        elif opcode == 4:
            result = register_b ^ register_c
            register_b = result
        elif opcode == 5:
            result = combo_operand % 8
            for c in str(result):
                results.append(c)
        elif opcode == 6:
            result = register_a / pow(2, combo_operand)
            register_b = int(result)
        elif opcode == 7:
            result = register_a / pow(2, combo_operand)
            register_c = int(result)
        op_index += 2

    return ",".join(results)


def part2(data):
    """Solve part 2."""
    number_sum = 0
    (register_a, register_b, register_c, program) = data

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
    puzzle = Puzzle(year=2024, day=17)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))