from aocd import get_data
puzzle_input = get_data(day=25, year=2022).split('\n')

snafu_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '=': -2,
    '-': -1
}

num_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '1=',
    4: '1-',
    5: '10',
    6: '11',
    7: '12',
    8: '2=',
    9: '2-'
}

def convert_snafu(snafu):
    snafu_pos = len(snafu) - 1
    number = 0
    for digit in snafu:
        number += snafu_dict[digit] * 5**snafu_pos 
        snafu_pos -= 1
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
