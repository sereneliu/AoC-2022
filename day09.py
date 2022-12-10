from aocd import get_data
puzzle_input = get_data(day=9, year=2022).split('\n')

def down(x, y):
     return x, y - 1

def up(x, y):
     return x, y + 1
     
def right(x, y):
     return x + 1, y

def left(x, y):
     return x - 1, y

def move(direction, start):
    x, y = start
    if direction == 'U':
        x, y = up(x, y)
    elif direction == 'D':
        x, y = down(x, y)
    elif direction == 'L':
        x, y = left(x, y)
    elif direction == 'R':
        x, y = right(x, y)
    return (x, y)

def realign_tail(old, new, head, tail):
    hx, hy = head
    tx, ty = tail
    if head == tail or \
        old == 'U' and new == 'D' or \
        old == 'D' and new == 'U' or \
        old == 'L' and new == 'R' or \
        old == 'R' and new == 'L' or \
        (abs(hx - hy) == 1 and abs(hy - hx) == 1):
        return tail
    elif old == new and (abs(hx - hy) == 2 or abs(hy - hx) == 2):
        tx, ty = move(old, tail)
    elif old == 'U' and new == 'R' or \
        old == 'R' and new == 'U':
        tx += 1
        ty += 1
    elif old == 'U' and new == 'L' or \
        old == 'L' and new == 'U':
        tx -= 1
        ty += 1
    elif old == 'D' and new == 'R' or \
        old == 'R' and new == 'D':
        tx += 1
        ty -= 1
    elif old == 'D' and new == 'L' or \
        old == 'L' and new == 'D':
        tx -= 1
        ty -= 1
    return (tx, ty)

visited = [(0, 0)]

def find_locations(directions):
    head = (0, 0)
    tail = (0, 0)
    prev_direction = directions[0][0]
    for direction in directions:
        current_direction = direction[0]
        steps = int(direction[2:])
        print("start", current_direction, steps, head, tail)
        head = move(current_direction, head)
        steps -= 1
        print("head moves", current_direction, steps, head, tail)
        if steps != 0:
            head = move(current_direction, head)
            tail = realign_tail(prev_direction, current_direction, head, tail)
            if tail not in visited:
                visited.append(tail)
            steps -= 1
            print("tail realigns", current_direction, steps, head, tail)
        while steps != 0:
            head = move(current_direction, head)
            tail = move(current_direction, tail)
            if tail not in visited:
                visited.append(tail)
            steps -= 1
            print(current_direction, steps, head, tail)
        prev_direction = current_direction

find_locations(puzzle_input)
print(len(visited))
