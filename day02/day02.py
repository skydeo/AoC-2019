import timeit

test = 0

with open('02.in', 'r+') as f:
  puzzle_input = [int(i) for i in f.read().split(',')]

test_input = [int(i) for i in "1,9,10,3,2,3,11,0,99,30,40,50".split(',')]


# Part One
def process_intcode(ins):
  pos = 0

  # Replace values
  ins[1] = 12
  ins[2] = 2

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

print(f"Program completed.\nValue at position 0: {process_intcode(puzzle_input)}")

# Part Two

