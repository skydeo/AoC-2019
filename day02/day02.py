import timeit

with open('02.in', 'r+') as f:
  puzzle_input = [int(i) for i in f.read().split(',')]

test_input = [int(i) for i in "1,9,10,3,2,3,11,0,99,30,40,50".split(',')]

# ins = test_input
ins = puzzle_input

# Part One
pos = 0
code = ins[pos]
# print(ins)

# Replace values
ins[1] = 12
ins[2] = 2


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
  # print(ins)

print(f"Program completed. Value at position 0: {ins[0]}")

