import timeit
from math import floor

with open('01.in', 'r+') as f:
  puzzle_input = [int(i) for i in f.read().splitlines()]

# Part One
start_time = timeit.default_timer()

def calculate_fuel_required(mass):
  return (floor(mass/3) - 2)

def fuel_for_modules(modules):
  return sum([calculate_fuel_required(m) for m in modules])

ffm = fuel_for_modules(puzzle_input)
print(f"Part 1: {ffm}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.")

# Part Two
start_time = timeit.default_timer()

def calculate_fuel_costs(mass):
  if calculate_fuel_required(mass) < 1:
    return 0
  else:
    fc = calculate_fuel_required(mass) + calculate_fuel_costs(calculate_fuel_required(mass))
    # print(f"Fuel cost for mass {mass} calculated at {fc}")
    return fc

tfr = sum([calculate_fuel_costs(m) for m in puzzle_input])
# tfr = calculate_fuel_costs(1969)
# print(calculate_fuel_required(21))
print(f"Part 2: {tfr}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.")

