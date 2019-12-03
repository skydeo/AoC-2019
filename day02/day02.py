import timeit

test = 0

with open('02.in', 'r+') as f:
  puzzle_input = [int(i) for i in f.read().split(',')]

test_input = [int(i) for i in "1,9,10,3,2,3,11,0,99,30,40,50".split(',')]


# Part One
def process_intcode(ins, noun, verb):
  pos = 0

  # Replace values
  ins[1] = noun
  ins[2] = verb

  code = ins[pos]

  while code != 99:
    a = ins[ins[pos+1]]
    b = ins[ins[pos+2]]
    store = ins[pos+3]
    if code == 1:
      ins[store] = a+b
    elif code == 2:
      ins[store] = a*b
    else:
      print(f"Error: code {code}")
      print(ins)
    pos += 4
    code = ins[pos]

  return ins[0]

start_time = timeit.default_timer()
print(f"Program completed.\nValue at position 0: {process_intcode(puzzle_input[:], 12, 2)}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.")

# Part Two
start_time = timeit.default_timer()

output = 19690720

for noun in range(0,100):
  for verb in range(0,100):
    if process_intcode(puzzle_input[:], noun, verb) == output:
      print(f"Magic value found: {100*noun+verb}")
      break
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.")

