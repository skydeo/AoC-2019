import timeit

with open('04.in', 'r+') as f:
  [minimum, maximum] = [int(i) for i in f.readline().rstrip().split('-')]

# minimum = 111122
# maximum = 123444

# Part One
def find_passwords(minimum, maximum):
  passwords = []

  for i in range(minimum, maximum+1):
    s = str(i)
    repeats = [s[pos-1] == s[pos] for pos in range(1,len(s))]
    if not any(repeats):
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
def find_passwords_strict(loose_passwords):
  strict_passwords = []

  for password in loose_passwords:
    s = str(password)
    for digit in s:
      if s.count(digit) == 2:
        strict_passwords.append(int(s))
        break
  
  return strict_passwords

start_time = timeit.default_timer()

strict_passwords = find_passwords_strict(passwords)

print(f"{len(strict_passwords)} passwords were found.")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.")
