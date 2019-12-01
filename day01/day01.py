import timeit
from math import floor

start_time = timeit.default_timer()

with open('01.in', 'r+') as f:
  puzzle_input = [int(i) for i in f.read().splitlines()]

fuel_required = sum([floor(m/3)-2 for m in puzzle_input])

print(f"The amount of fuel required is {fuel_required}")
