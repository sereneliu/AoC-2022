puzzle_input = open('day05.txt', 'r').read().split('\n')

stacks = {}
rearrangement_procedure = []

def split_crates(row):
    return [row[i:i+3] for i in range(0, len(row), 4)]

def init(drawing):
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

def remove_empty():
    for i in range(len(stacks.keys())):
        stack = stacks[i + 1]
        while '   ' in stack:
            stacks[i + 1].remove('   ')

def move_crate(no_of_crates, starting_stack, ending_stack):
    # print("move", no_of_crates, 'crates')
    for i in range(no_of_crates):
        # print("from", starting_stack, stacks[starting_stack])
        # print("to", ending_stack, stacks[ending_stack])
        stacks[ending_stack].append(stacks[starting_stack][-1])
        stacks[starting_stack].pop()

def find_final_arrangement(instructions):
    for instruction in instructions:
        move_crate(instruction[0], instruction[1], instruction[2])

def get_top_crates():
    top_crates = ''
    for i in range(len(stacks.keys())):
        stack = stacks[i + 1]
        top_crates += stack[-1].strip('[]')
    return top_crates

def part1(input):
    init(input)
    remove_empty()
    find_final_arrangement(rearrangement_procedure)
    return get_top_crates()

print(part1(puzzle_input)) # QPJPLMNNR
