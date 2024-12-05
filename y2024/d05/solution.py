from aocd.models import Puzzle


def parse(data):
    (rules, pages) = data.split("\n\n")
    rules = rules.split()
    rules1 = []
    for rule in rules:
        rules1.insert(0, rule.split("|"))

    return rules1, pages.split()


def in_right_order(step_index, steps, rules):
    applied_rules = list(filter(lambda x: x[1] == steps[step_index], rules))
    # print("{} {} {} {}".format(steps[step_index], applied_rules, steps[step_index + 1::], step_index))
    for rule in applied_rules:
        if step_index + 1 < len(steps):
            if steps[step_index + 1:].count(rule[0]) > 0:
                return False, steps.index(rule[0])
    return True, -1


def part1(data):
    """Solve part 1."""
    # print(data[0])
    number_sum = 0
    rules = data[0]
    pages = data[1]
    for page in pages:
        steps = page.split(",")
        page_is_right = True
        for step_index in range(len(steps)):
            if not in_right_order(step_index, steps, rules)[0]:
                page_is_right = False
                break

        if page_is_right:
            number_sum += int(steps[round((len(steps) - 1)/2)])

    return number_sum


def order_in_right_order(step_index, steps, rules, is_rightly_ordered):
    if step_index + 1 < len(steps):
        (b, i) = in_right_order(step_index, steps, rules)
        if b:
            return order_in_right_order(step_index + 1, steps, rules, is_rightly_ordered)
        else:
            new_steps = steps.copy()
            value = steps[i]
            del new_steps[i]
            new_steps.insert(step_index, value)

            return order_in_right_order(step_index, new_steps, rules, False)
    else:
        if is_rightly_ordered:
            return 0
        else:
            # print("{} {}:{}".format(steps, steps[round((len(steps) - 1)/2)], round((len(steps) - 1)/2)))
            return int(steps[round((len(steps) - 1)/2)])

def part2(data):
    """Solve part 2."""
    number_sum = 0
    rules = data[0]
    pages = data[1]
    for page in pages:
        steps = page.split(",")
        number_sum += order_in_right_order(0, steps, rules, True)


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
    if solution2 == int(123):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 31))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=5)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

