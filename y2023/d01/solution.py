from aocd.models import Puzzle


# for practice so that I know slightly what I am trying to do
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def parse(data):
    return data.split()


def part1(data):
    """Solve part 1."""
    number_sum = 0
    for row in data:
        filtered = filter(str.isdigit, row)
        string_digit = "".join(filtered)
        number_sum = number_sum + int(string_digit[0] + string_digit[len(string_digit) - 1])

    return number_sum


def check_string_for_numbers(string, number_list):
    name = ""
    for number in number_list:
        if number in string:
            name = number
            break

    if name == "":
        return 0
    else:
        return int(number_list.index(name)) + 1


def part2(data):
    """Solve part 2."""
    number_sum = 0
    for row in data:
        first = ""
        second = ""
        for i in range(len(row)):
            c = row[i]
            characters = row[:i+1]
            if c.isdigit():
                first = "".join(c)
                break
            else:
                if check_string_for_numbers(characters, numbers) != 0:
                    index = check_string_for_numbers(characters, numbers)
                    first = str(index)
                    break
        print(first)
        for j in range(len(row)):
            c = row[-j - 1]
            characters = row[-j - 1:]
            if c.isdigit():
                second = "".join(c)
                break
            else:
                if check_string_for_numbers(characters, numbers) != 0:
                    index = check_string_for_numbers(characters, numbers)
                    second = str(index)
                    break

        number_sum = number_sum + int(first + second)

    return number_sum


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    print(data)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=1)
    print(puzzle.examples[1])
    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

    if solutions[0] == int(puzzle.answer_a):
        print("A WENT RIGHT!")
    else:
        print("A went wrong! " + puzzle.answer_a)

    if solutions[1] == int(puzzle.answer_b):
        print("B WENT RIGHT!")
    else:
        print("B went wrong! " + puzzle.answer_b)
