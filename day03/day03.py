import timeit
import operator

test = 0

with open("03.in", "r+") as f:
  puzzle_input = f.read().splitlines()
  wire1 = puzzle_input[0].split(",")
  wire2 = puzzle_input[1].split(",")

if test:
  # wire1 = "R8,U5,L5,D3".split(",")
  # wire2 = "U7,R6,D4,L4".split(",")
  wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
  wire2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

# Part One
def plot_wire_path(ins):
  trans = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1)
    }

  points = set()
  last = (0,0)

  for i in ins:
    direction = trans[i[0]]
    l = int(i[1:])

    for _ in range(0,l):
      last = tuple(map(operator.add, last, direction))
      points.add(last)
  
  return points


def find_overlaps(path1, path2):  
  return path1 & path2


def find_closest_overlap_md(overlaps):
  ordered = sorted(overlaps, key=lambda x: abs(x[0]) + abs(x[1]))
  return abs(ordered[0][0]) + abs(ordered[0][1])


start_time = timeit.default_timer()

overlaps = find_overlaps(plot_wire_path(wire1), plot_wire_path(wire2))
closest_md = find_closest_overlap_md(overlaps)

print(f"Manhattan Distance to closest overlap: {closest_md}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.")

