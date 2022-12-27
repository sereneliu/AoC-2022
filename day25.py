from aocd import get_data
puzzle_input = get_data(day=25, year=2022).split('\n')

snafu_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '=': 3,
    '-': 4
}

num_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '=',
    4: '-',
    5: '10',
    6: '11',
    7: '12',
    8: '1=',
    9: '1-'
}

def convert_snafu(snafu):
    snafu_pos = len(snafu)
    number = 0
    for digit in snafu:
        number += snafu_dict[digit] * snafu_pos * 5
    return number

def convert_number(number):
    snafu = ''
    for digit in str(number):
        snafu += num_dict[int(digit)]
    return snafu

def part1(fuel_reqs):
    snafu_sum = 0
    for fuel_req in fuel_reqs:
        snafu_sum += convert_snafu(fuel_req)
    return convert_number(snafu_sum)

print(part1(puzzle_input))
