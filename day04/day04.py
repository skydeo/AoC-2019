import timeit

with open('04.in', 'r+') as f:
  [minimum, maximum] = [int(i) for i in f.readline().rstrip().split('-')]

# minimum = 100000
# maximum = 111112

# Part One
def find_passwords(minimum, maximum):
  passwords = []

  for i in range(minimum, maximum+1):
    s = str(i)
    if not any([s[pos-1] == s[pos] for pos in range(1,len(s))]):
      pass
    elif any([int(s[pos-1]) > int(s[pos]) for pos in range(1,len(s))]):
      pass
    else:
      passwords.append(int(s))
  
  return passwords

start_time = timeit.default_timer()

passwords = find_passwords(minimum, maximum)

print(f"{len(passwords)} passwords were found.")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.")

# Part Two
