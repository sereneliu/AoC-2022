from aocd import get_data
puzzle_input = get_data(day=10, year=2022).split('\n')

def store_v_values(program):
    v_values = []
    v_values.append(0)
    for line in program:
        v_values.append(0)
        if line.startswith('addx'):
            v = int(line[5:])
            v_values.append(v)
    return v_values

def find_signal_strengths(v, cycles):
    sum = 0
    x = 1
    for cycle in range(cycles):
        x += v[cycle]
        if (cycle -19) % 40 == 0:
            sum += ((cycle + 1) * x)
    return sum

v_values = store_v_values(puzzle_input)
print(find_signal_strengths(v_values, 220)) # 13060

def draw_pixels(v, cycles):
    image = ''
    x = 1
    for cycle in range(cycles):
        x += v[cycle]
        sprite = (x - 1, x, x + 1)
        if cycle % 40 in sprite:
            image += '#'
        else:
            image += '.'
    print(image[0:40])
    print(image[40:80])
    print(image[80:120])
    print(image[120:160])
    print(image[160:200])
    print(image[200:])

draw_pixels(v_values, 240) # FJUBULRZ