from aocd import get_data
puzzle_input = get_data(day=24, year=2022)
puzzle_input = puzzle_input.split('\n')

def down(x, y):
     return x, y + 1

def up(x, y):
     return x, y - 1
     
def right(x, y):
     return x + 1, y

def left(x, y):
     return x - 1, y

def find_initial_positions(map):
    initial_positions = {}
    x = 0
    y = 0
    for row in map:
        for position in row:
            initial_positions[(x, y)] = position
            x += 1
        x = 0        
        y += 1
    return initial_positions

# print(find_initial_blizzards(puzzle_input))

def move_blizzard(map):
    directions = ['v', '^', '>', '<']
    for key, value in map.items():
        if direction in directions:
            direction = value
            x, y = key
            if direction == 'v':
                if y == 151:
                    y = 0
                x, y = down(x, y)
            elif direction == '^':
                if y == 0:
                    y = 151
                x, y = up(x, y)
            elif direction == '>':
                if x == 151:
                    x = 0
                x, y = right(x, y)
            elif direction == '<':
                if x == 0:
                    x = 151
                x, y = left(x, y)
            map[(x,y)] = direction
    return map

def move_exposition(x, y):
    potential_moves = [(x, y)]
    if up(x, y) == '.':
        potential_moves.append(up(x, y))
    if down(x, y) == '.':
        potential_moves.append(down(x, y))
    if right(x, y) == '.':
        potential_moves.append(right(x, y))
    if left(x, y) == '.':
        potential_moves.append(left(x, y))
    if len(potential_moves) <= 2:
        return potential_moves[-1]
    elif len(potential_moves) > 2:
        print('not sure what to do here yet')

def part1(map):
    all_positions = find_initial_positions(map)
    min = 0
    start = (map[0].index('.'), 0)
    end = (map[-1].index('.'), len(map) - 1)
    exposition = start
    while exposition != end:
        move_blizzard(all_positions)
        move_exposition(exposition)
        min += 1
    return min
