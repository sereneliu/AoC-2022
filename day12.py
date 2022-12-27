from aocd import get_data
from collections import defaultdict

puzzle_input = get_data(day=12, year=2022).split('\n')

def down(x, y):
     return x, y + 1

def up(x, y):
     return x, y - 1
     
def right(x, y):
     return x + 1, y

def left(x, y):
     return x - 1, y

coords = {}

def save_heights(heightmap):
  x = 0
  y = 0
  for row in heightmap:
    for height in row:
      x += 1
      coords[(x, y)] = height
    y += 1

save_heights(puzzle_input)
print(coords)
