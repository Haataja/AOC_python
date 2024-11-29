from aocd import get_data
from aocd.models import Puzzle

x = get_data(day=1, year=2023)

y = Puzzle(year=2023, day=1)
print(y.examples[0].input_data)
