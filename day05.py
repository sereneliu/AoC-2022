from copy import deepcopy

puzzle_input = open('day05.txt', 'r').read().split('\n')

def split_crates(row):
    return [row[i:i+3] for i in range(0, len(row), 4)]

def init(drawing):
    stacks = {}
    rearrangement_procedure = []
    for i in range(len(split_crates(drawing[0]))):
        stacks[i + 1] = []
    for row in drawing:
        if row.startswith("move"):
            instruction = (int(row[row.index('move') + 5:row.index(' from')]), int(row[row.index('from') + 5]), int(row[row.index('to') + 3]))
            rearrangement_procedure.append(instruction)
        elif not row.startswith(" 1"):
            crates_in_row = split_crates(row)
            i = 1
            for crate in crates_in_row:
                stacks[i].insert(0, crate)
                i += 1
    stacks = remove_empty(stacks)
    return stacks, rearrangement_procedure

def remove_empty(stacks_with_empty):
    for i in range(len(stacks_with_empty.keys())):
        stack = stacks_with_empty[i + 1]
        while '   ' in stack:
            stacks_with_empty[i + 1].remove('   ')
    return stacks_with_empty

def move_crate(all_stacks, no_of_crates, starting_stack, ending_stack):
    for i in range(no_of_crates):
        all_stacks[ending_stack].append(all_stacks[starting_stack][-1])
        all_stacks[starting_stack].pop()

def move_crate2(all_stacks, no_of_crates, starting_stack, ending_stack):
    all_stacks[ending_stack] += all_stacks[starting_stack][-1 * no_of_crates:]
    all_stacks[starting_stack] = all_stacks[starting_stack][:-1 * no_of_crates]

def find_final_arrangement(all_stacks, instructions, is_new):
    for instruction in instructions:
        if is_new:
            move_crate2(all_stacks, instruction[0], instruction[1], instruction[2])
        else:
            move_crate(all_stacks, instruction[0], instruction[1], instruction[2])

def get_top_crates(stack_arrangement):
    top_crates = ''
    for i in range(len(stack_arrangement.keys())):
        stack = stack_arrangement[i + 1]
        top_crates += stack[-1].strip('[]')
    return top_crates

def part1(all_stacks, instructions):
    find_final_arrangement(all_stacks, instructions, False)
    return get_top_crates(all_stacks)

def part2(all_stacks, instructions):
    find_final_arrangement(all_stacks, instructions, True)
    return get_top_crates(all_stacks)

def both(puzzle_input):
    initial_stacks, rearrange_procedure = init(puzzle_input) # MHGSNWWVF
    stacks = deepcopy(initial_stacks)
    print(get_top_crates(stacks))
    print(part1(stacks, rearrange_procedure)) # QPJPLMNNR
    print(part2(initial_stacks, rearrange_procedure)) # BQDNWJPVJ

both(puzzle_input)
