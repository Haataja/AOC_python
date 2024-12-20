from aocd.models import Puzzle
import functools

def parse(data):
    return list(map(lambda x: int(x), data.split()))


def part1(data, blinks):
    """Solve part 1."""
    number_sum = 0
    # print(data)
    for index in range(blinks):
        # print(index)
        stone_index = 0
        while stone_index < len(data):
            if data[stone_index] == 0:
                data[stone_index] = 1
                # print("ADDED 1 to zero: {}".format(data))
            elif len(str(data[stone_index])) % 2 == 0:
                str_stone = str(data[stone_index])
                half = int(len(str_stone) / 2)
                first_stone = int(str_stone[:half])
                second_stone = int(str_stone[half:])
                # print(first_stone, second_stone)
                del data[stone_index]
                if stone_index == 0:
                    data.insert(stone_index, first_stone)
                    data.insert(1, second_stone)
                else:
                    data.insert(stone_index, second_stone)
                    data.insert(stone_index, first_stone)
                if stone_index + 1 < len(data):
                    stone_index = stone_index + 1
                # print("ADDED stone: {}".format(data))
            else:
                data[stone_index] = data[stone_index] * 2024
                # print("Multiplied by 2024: {}".format(data))
            stone_index += 1
    # print(data)
    return len(data)

# https://www.reddit.com/r/adventofcode/comments/1hbnyx1/2024_day_11python_mega_tutorial/
@functools.lru_cache(maxsize=None)
def calc_number_of_stones_after_blinks(stone, blink, max_blinks):
    if blink == max_blinks:
        if len(str(stone)) % 2 == 0:
            return 2
        else:
            return 1

    second_stone = -1
    if stone == 0:
        first_stone = 1
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        half = int(len(str_stone) / 2)
        first_stone = int(str_stone[:half])
        second_stone = int(str_stone[half:])
    else:
        first_stone = stone * 2024

    sum_of_stones = calc_number_of_stones_after_blinks(first_stone, blink + 1, max_blinks)
    if second_stone != -1:
        sum_of_stones += calc_number_of_stones_after_blinks(second_stone, blink + 1, max_blinks)
    return sum_of_stones


def part2(data):
    """Solve part 2."""
    number_sum = 0
    for stone in data:
        print("Part 2: {}".format(stone))
        number_sum += calc_number_of_stones_after_blinks(stone, 0, 74)

    return number_sum


def solve(puzzle_data):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_data)
    data1 = data.copy()
    solution1 = part1(data1, 25)
    data2 = data.copy()
    solution2 = part2(data2)

    return solution1, solution2


def test():
    orig_data = parse("125 17")
    test1_data = orig_data.copy()
    solution1 = part1(test1_data, 25)
    if solution1 == int(puzzle.examples[0].answer_a):
        print("TEST 1: YES!")
    else:
        print("was {} should have been {}".format(solution1, puzzle.examples[0].answer_a))

    """test2_data = parse("125 17")
    solution2 = part2(test2_data)
    if solution2 == int(puzzle.examples[0].answer_a):
        print("TEST 2: YES!")
    else:
        print("was {} should have been {}".format(solution2, 31))"""


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=11)
    print(puzzle.examples)
    test()

    puzzle_input = puzzle.input_data
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

