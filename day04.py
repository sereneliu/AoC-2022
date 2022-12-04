puzzle_input = open('day04.txt', 'r').read().split('\n')

# Part 1

def parse_sections(sections, symbol):
    part1 = sections[:sections.index(symbol)]
    part2 = sections[sections.index(symbol) + 1:]
    part2 = part2.strip()
    return (part1, part2)

def has_overlap(section_pair, is_full):
    elf1, elf2 = parse_sections(section_pair, ",")
    elf1_start, elf1_end = parse_sections(elf1, "-")
    elf2_start, elf2_end = parse_sections(elf2, "-")

    if is_full:
        if (int(elf1_start) <= int(elf2_start) and int(elf1_end) >= int(elf2_end)) or \
            (int(elf2_start) <= int(elf1_start) and int(elf2_end) >= int(elf1_end)):
            return True
    else:
        if (int(elf1_start) <= int(elf2_start) and int(elf1_end) >= int(elf2_start)) or \
            (int(elf2_start) <= int(elf1_start) and int(elf2_end) >= int(elf1_start)) or \
            (int(elf1_start) <= int(elf2_end) and int(elf1_end) >= int(elf2_end)) or \
            (int(elf2_start) <= int(elf1_end) and int(elf2_end) >= int(elf1_end)):
            return True
    
    return False

def find_overlaps(all_pairs, is_full):
    overlaps = 0
    for pair in all_pairs:
        if has_overlap(pair, is_full):
            overlaps += 1
    return overlaps

print(find_overlaps(puzzle_input, True)) # 471

# Part 2

print(find_overlaps(puzzle_input, False)) # 888
