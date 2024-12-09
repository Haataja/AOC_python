from aocd.models import Puzzle


def parse(data):
    id_number = 0
    is_space = False
    checksum_list = []
    for d in data:
        d_number = int(d)
        for number in range(d_number):
            if is_space:
                checksum_list.append(".")
            else:
                checksum_list.append(id_number)
        if not is_space:
            id_number += 1
        is_space = not is_space
    return checksum_list


def part1(data):
    checksum_list = data.copy()
    """Solve part 1."""
    number_sum = 0
    print("start part 1")
    while checksum_list.count(".") > 0:
        last = checksum_list.pop()
        if last != ".":
            index = checksum_list.index(".")
            del checksum_list[index]
            checksum_list.insert(index, last)
    print("list ordered, calculating checksum")
    for cs_index in range(len(checksum_list)):
        number_sum += cs_index * checksum_list[cs_index]
    print("Check sum calculated")
    return number_sum


def remove_old_instances(number, checksum_list):
    for index in range(len(checksum_list)):
        if checksum_list[index] == number:
            checksum_list[index] = "."


def search_and_replace(number, count, index, checksum_list):
    search = checksum_list[index:]
    search.reverse()
    search_count = 0
    for search_index in range(len(search)):
        if search[search_index] == ".":
            search_count += 1
            # print("{} searching {}".format(search_index, search_count))
            if search_count == count:
                remove_old_instances(number, checksum_list)
                for insert_number in range(count):
                    replace_index = - search_index - 1 + insert_number
                    # print("index: {}, replace index {},".format(search_index, replace_index))
                    del checksum_list[replace_index]
                    checksum_list.insert(replace_index + 1, number)
                break

        else:
            search_count = 0


def part2(data):
    checksum_list = data.copy()
    """Solve part 2."""
    number_sum = 0
    print("start part 2".format(data))

    checksum_list.reverse()
    current = 0
    current_count = 1
    for index in range(len(checksum_list) - 1):
        current = checksum_list[index]
        if checksum_list[index + 1] != current:
            search_and_replace(current, current_count, index, checksum_list)
            # print("replaced {} {} : {}".format(current, current_count, checksum_list))
            current_count = 1
        else:
            current_count += 1
    checksum_list.reverse()
    print("Got in order")
    for index in range(len(checksum_list)):
        if checksum_list[index] != ".":
            number_sum += index * checksum_list[index]

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
    if solution2 == int(2858):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 2858))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=9)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

