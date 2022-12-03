puzzle_input = open('day03.txt', 'r').read().split('\n')

# Part 1

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def find_common(group):
    return ''.join(set(group[0]).intersection(*group))

def sum_priorities(rucksacks):
    sum = 0
    for rucksack in rucksacks:
        items_no = len(rucksack)//2
        compt1 = rucksack[:items_no]
        compt2 = rucksack[items_no:]
        priority = find_common((compt1, compt2))
        sum += alphabet.index(priority) + 1
    return sum

print(sum_priorities(puzzle_input)) # 7917

# Part 2

def sum_badges(rucksacks):
    sum = 0
    for i in range(0, len(rucksacks), 3):
        badge = find_common((rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]))
        sum += alphabet.index(badge) + 1
    return sum

print(sum_badges(puzzle_input)) # 2585
