puzzle_input = open('day1.txt', 'r').read().split('\n')
puzzle_input = [int(n) for n in puzzle_input]

def find_measurement_increases(measurements, window):
    prev_measurement_total = sum(measurements[0:window])
    larger_measurements = 0
    for i in range(len(measurements)):
        new_measurement_total = sum(measurements[i:i + window])
        if new_measurement_total > prev_measurement_total:
            larger_measurements += 1
        prev_measurement_total = new_measurement_total
    return larger_measurements

# Part 1
print(find_measurement_increases(puzzle_input, 1))

# Part 2
print(find_measurement_increases(puzzle_input, 3))
